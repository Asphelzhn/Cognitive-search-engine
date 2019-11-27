import json
from detecht_api.detecht_converter.section_class import *
from detecht_api.detecht_converter.keyword_class import *
from detecht_api.detecht_nlp.imp_sent_creator import imp_sent_creator
from detecht_api.detecht_es.insert_file import inject_one_file
from detecht_api.detecht_nlp.keywordExtraction.yake_api import Yake4Keyword
from detecht_api.detecht_converter.pdf_converter import pdf_extractor
from detecht_api.detecht_db_handling import keyword as db_keyword


# Jakob, Carl, Oscar and Henrik
class JsonClass:

    def __init__(self, pdf_name, title, date_created, pages=list()):
        self.pdf_name = pdf_name
        self.title = title
        self.keywords = list()
        self.pages = pages
        self.date_created = date_created

    @classmethod
    def init_from_json(cls, json_file):
        json_doc = json.loads(json_file)
        json_obj = cls(json_doc["pdf_name"], json_doc["title"], json_doc["date_created"], json_doc["pages"])

        for keyword in json_doc["keywords"]:
            json_obj.keywords.append(keyword_class(keyword["Keyword"], keyword["Weight"]))
        return json_obj

    @classmethod
    def init_from_pdf(cls, pdf_name, title, tags):
        pdf_extraction = pdf_extractor(pdf_name)
        date_created = pdf_extraction[1]
        pages = pdf_extraction[0]
        json_obj = cls(pdf_name, title, date_created, pages)

        keywords_list = Yake4Keyword.yake_api(json_obj.get_all_plaintext(), pdf_name)
        for keyword in keywords_list:
            # TODO make the following work (the ones that created the database functionality)
            db_keyword.addKeyword(keyword[0])
            db_keyword.Add_Pdf_Name_Keyword_Weight(pdf_name, keyword[0], float(keyword[1]))
            json_obj.add_keyword(keyword[0], keyword[1])

        # TODO make the following work (the ones that created the database functionality)
        db_keyword.add_pdf_similarities(pdf_name)
        return json_obj

    def get_all_plaintext(self):  # return plain text from entire pdf
        full_text = ""
        for page in self.pages:
            full_text += page
        return full_text

    def get_plaintext(self, start_page, end_page):  # return plain text from start_page to end_page
        segment_text = ""
        iteration_amount = end_page - start_page
        for i in range(iteration_amount):
            segment_text = segment_text + self.pages[start_page + i]
        return segment_text

    def frontend_result(self, query):
        keywords = []
        for keyword in self.keywords:
            keywords.append({'keyword': keyword.get_keyword(), 'weight': keyword.get_weight()})
        return {'pdfTitle': self.title, 'pdfName': self.pdf_name, 'keywords': keywords}

    def get_json_object(self):
        keywords_tmp = list()
        for keyword_tmp in self.keywords:
            keywords_tmp.append(keyword_tmp.get_keyword_dict())
        a = {
            'pdf_name': self.pdf_name,
            'title': self.title,
            'keywords': keywords_tmp,
            'pages': self.pages,
            'date_created': self.date_created}
        return json.dumps(a)

    # Adds whole document to one string, can be a problem with memory management
    def get_date_created(self):
        return self.date_created

    def add_title(self, title):
        self.title = title

    def add_keyword(self, keyword, weight):
        self.keywords.append(keyword_class(keyword, weight))

    def get_keywords(self):
        return self.keywords

    def set_pdf_name(self, pdfname):
        self.pdf_name = pdfname

    def get_pdf_name(self):
        return self.pdf_name

    # Henrik
    def get_abstract(self, query):
        sent_array = imp_sent_creator(self.get_all_plaintext(), query, 3)
        abstract = []
        for sentence in sent_array:
            abstract.append({'sentence': str(sentence.sent)})
        return abstract

    # Jakob
    def inject_to_es(self):
        inject_one_file(self.get_json_object())

# Commented this since we wont be using sections (Carl and Oscar) told me Nicklas that I think
    # def add_pages(self):
    #     json_tmp = json.loads(self.pdf_name.read())
    #     attr = str
    #     attr = (json_tmp["pages"])  # collect attribute
    #
    #     index = 0
    #     for i in attr:
    #         self.sections.append([i, index])
    #         index += len(i)
