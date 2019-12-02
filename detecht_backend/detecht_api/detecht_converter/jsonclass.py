import json
import ast
import spacy
import datetime
# from detecht_api.detecht_converter.section_class import *
from detecht_api.detecht_converter.keyword_class import keyword_class
# from detecht_api.detecht_nlp.imp_sent_creator import imp_sent_creator
from detecht_api.detecht_es.insert_file import inject_one_file
from detecht_api.detecht_nlp.keywordExtraction.yake_api import Yake4Keyword
from detecht_api.detecht_converter.pdf_converter import pdf_extractor
from detecht_api.detecht_nlp.abstract import imp_sent_api
from detecht_api.detecht_nlp.abstract.class_imp_set import ImpSent
from detecht_api.detecht_db_handling import keyword as db_keyword
from detecht_api.detecht_nlp.spell_check import createTxt
from detecht_api.detecht_nlp.autocompleteWords import upload_n_gram

abstract = imp_sent_api.imp_sent_api()
nlp = spacy.load("en_core_web_sm")


# Jakob, Carl, Oscar and Henrik
class JsonClass:

    def __init__(self, pdf_name, title, date_created,
                 databaseObject, word_frequencies=dict(),
                 pages=list()):
        self.pdf_name = pdf_name
        self.title = title
        self.keywords = list()
        self.pages = pages
        self.date_created = date_created
        self.databaseObject = databaseObject
        self.word_frequencies = word_frequencies

    @classmethod
    def init_from_json(cls, json_file):
        json_doc = json.loads(json_file)
        databaseObjTemp = list()
        for imp_doc in json_doc["databaseObject"]:
            imp_obj = ImpSent()
            # imp_obj.set_sent(imp_doc['sent'])
            imp_obj.set_sent(nlp(imp_doc['sent']))
            imp_obj.rank = imp_doc['rank']
            imp_obj.order = imp_doc['order']
            imp_obj.start_index = imp_doc['start_index']
            imp_obj.end_index = imp_doc['end_index']
            imp_obj.score = imp_doc['score']
            imp_obj.page = imp_doc['page']
            databaseObjTemp.append(imp_obj)

        json_obj = cls(json_doc["pdf_name"],
                       json_doc["title"],
                       json_doc["date_created"],
                       databaseObjTemp,
                       ast.literal_eval(json_doc["word_frequencies"]),
                       json_doc["pages"])

        for keyword in json_doc["keywords"]:
            json_obj.keywords.append(keyword_class(keyword["Keyword"],
                                                   keyword["Weight"]))
        return json_obj

    @classmethod
    def init_from_pdf(cls, pdf_name, title, tags):
        pdf_extraction = pdf_extractor(pdf_name)
        date_created = None
        try:
            datetime.datetime.strftime(pdf_extraction[1], '%Y-%m-%d')
            date_created = pdf_extraction[1]
        except ValueError:
            date_created = datetime.date.today().strftime('%Y-%m-%d')
        pages = pdf_extraction[0]
        createTxt.creteTxt(pages)
        upload_n_gram.upload()
        databaseObject, word_frequencies = abstract\
            .upload_find_relevant_sentences(pages)
        json_obj = cls(pdf_name,
                       title,
                       date_created,
                       databaseObject,
                       word_frequencies,
                       pages)

        keywords_list = Yake4Keyword.yake_api(json_obj.get_all_plaintext(),
                                              pdf_name)
        for keyword in keywords_list:
            # TODO make the following work (the ones that created
            #  the database functionality)
            db_keyword.addKeyword(keyword[0])
            db_keyword.Add_Pdf_Name_Keyword_Weight(pdf_name,
                                                   keyword[0],
                                                   float(keyword[1]))
            json_obj.add_keyword(keyword[0], keyword[1])

        # TODO make the following work (the ones that created
        #  the database functionality)
        db_keyword.add_pdf_similarities(pdf_name)
        return json_obj

    def get_all_plaintext(self):  # return plain text from entire pdf
        full_text = ""
        for page in self.pages:
            full_text += page
        return full_text

    def get_plaintext(self, start_page, end_page):  # return plain text
        # from start_page to end_page
        segment_text = ""
        iteration_amount = end_page - start_page
        for i in range(iteration_amount):
            segment_text = segment_text + self.pages[start_page + i]
        return segment_text

    def frontend_result(self, query):
        keywords = []
        for keyword in self.keywords:
            keywords.append({'keyword': keyword.get_keyword(),
                             'weight': keyword.get_weight()})
        return {'pdfTitle': self.title, 'pdfName': self.pdf_name,
                'keywords': keywords}

    def get_json_object(self):
        keywords_tmp = list()
        for keyword_tmp in self.keywords:
            keywords_tmp.append(keyword_tmp.get_keyword_dict())
        databaseObjTemp = list()
        for imp_obj in self.databaseObject:
            imp_obj_temp = {
                'sent': str(imp_obj.sent),
                'rank': imp_obj.rank,
                'order': imp_obj.order,
                'start_index': imp_obj.start_index,
                'end_index': imp_obj.end_index,
                'score': imp_obj.score,
                'page': imp_obj.page
            }
            databaseObjTemp.append(imp_obj_temp)
        a = {
            'pdf_name': self.pdf_name,
            'title': self.title,
            'keywords': keywords_tmp,
            'pages': self.pages,
            'databaseObject': databaseObjTemp,
            'word_frequencies': str(self.word_frequencies),
            'date_created': self.date_created}
        return json.dumps(a)

    # Adds whole document to one string,
    # can be a problem with memory management
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

    # Samuel
    def get_abstract(self, query):
        return abstract.generateAbstract(query,
                                         self.databaseObject,
                                         self.word_frequencies)

    # Jakob
    def inject_to_es(self):
        inject_one_file(self.get_json_object())

# Commented this since we wont be using sections (Carl and Oscar)
# told me Nicklas that I think
# def add_pages(self):
#     json_tmp = json.loads(self.pdf_name.read())
#     attr = str
#     attr = (json_tmp["pages"])  # collect attribute
#
#     index = 0
#     for i in attr:
#         self.sections.append([i, index])
#         index += len(i)
