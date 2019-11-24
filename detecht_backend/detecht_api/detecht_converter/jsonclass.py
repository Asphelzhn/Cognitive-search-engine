import json
from detecht_api.detecht_converter.section_class import *
from detecht_api.detecht_converter.keyword_class import *
from detecht_api.detecht_nlp.imp_sent_creator import imp_sent_creator
from detecht_api.detecht_es.insert_file import inject_one_file
from detecht_api.detecht_nlp.keywordExtraction.yake_api import Yake4Keyword
from detecht_api.detecht_converter.pdf_converter import pdf_extractor

# Jakob, Carl, Oscar and Henrik
class JsonClass:

    def __init__(self, pdf_name, title, tags):
        self.pdf_name = pdf_name
        self.title = title
        self.tags = tags
        self.keywords = list()
        self.pages = pdf_extractor(self.pdf_name)[0]
        self.date_created = pdf_extractor(self.pdf_name)[1]
        self.full_text = ""

        for page in self.pages:
            self.full_text +=page

    @classmethod
    def init_from_json(cls, json_file):
        json_doc = json.loads(json_file)
        json_obj = cls(json_doc["pdf_name"], json_doc["title"], json_doc["full_text"])

        for keyword in json_doc["keywords"]:
            json_obj.keywords.append(keyword_class(keyword["Keyword"], keyword["Weight"]))
        for tag in json_doc["tags"]:
            json_obj.add_tag(tag)
        for section in json_doc["sections"]:
            json_obj.add_section(section["start"], section["end"], section["section_keyword"])
        return json_obj

    @classmethod
    def init_from_pdf(cls, pdf_name, title, tags):
        json_obj = cls(pdf_name, title)

        keywords_list = Yake4Keyword.yake_api(json_obj.full_text, pdf_name)
        for keyword in keywords_list:
            json_obj.add_keyword(keyword[0], keyword[1])

        for tag in tags:
            json_obj.add_tag(tag)

        return json_obj

    def get_all_plaintext(self):
        # should return all pages

    def get_plaintext(start_page, end_page):
        # should return plain text from start_page to end_page


    def frontend_result(self, query):
        return {'pdfTitle': self.title, 'pdfName': self.pdf_name, 'abstract': self.get_abstract(query)}

    def get_json_object(self):
        keywords_tmp = list()
        for keyword_tmp in self.keywords:
            keywords_tmp.append(keyword_tmp.get_keyword_dict())
        sections_tmp = list()
        for section_tmp in self.sections:
            sections_tmp.append(section_tmp.get_section_dict())
        a = {
            'pdf_name': self.pdf_name,
            'title': self.title,
            'tags': self.tags,
            'keywords': keywords_tmp,
            'sections': sections_tmp,
            'full_text': self.full_text
            'pages' :self.pages
            'date_created': self.date_created}
        return json.dumps(a)

    def export_json(self, file_name=""):
        if file_name == "":
            file_name = self.pdf_name
        keywords_tmp = list()
        for keyword_tmp in self.keywords:
            keywords_tmp.append(keyword_tmp.get_keyword_dict())
        sections_tmp = list()
        for section_tmp in self.sections:
            sections_tmp.append(section_tmp.get_section_dict())
        a = {
            'pdf_name': self.pdf_name,
            'title': self.title,
            'tags': self.tags,
            'keywords': keywords_tmp,
            'sections': sections_tmp,
            'full_text': self.full_text}
        with open(file_name + ".json", 'w') as outfile:
            json.dump(a, outfile, indent=2)

    # Adds whole document to one string, can be a problem with memory management
    def get_date_created(self):
        return self.date_created

    def add_title(self, title):
        self.title = title

    def add_tag(self, tag):
        if tag not in self.tags:
            self.tags.append(tag)

    def remove_tag(self, tag):
        if tag in self.tags:
            self.tags.remove(tag)

    def get_tags(self):
        return self.tags

    def add_keyword(self, keyword, weight):
        self.keywords.append(keyword_class(keyword, weight))

    def get_keywords(self):
        return self.keywords

    def set_pdf_name(self, pdfname):
        self.pdf_name = pdfname

    def get_pdf_name(self):
        return self.pdf_name

    #
    def add_section(self, start, end, section_keywords):
        if start < end:
            section_tmp = section_class(start, end)
            for keyword in section_keywords:
                section_tmp.add_keyword(keyword["keyword"], keyword["weight"])
            self.sections.append(section_tmp)
        else:
            raise ValueError('End index can not be lower than start index.')

    def get_section_object(self, start, end):
        for section in self.sections:
            if section.get_start() == start & section.get_end() == end:
                return section
        raise ValueError('No matching section exists')

    def get_section_by_id(self, int):
        return self.sections[int]

    def get_sections(self):
        return self.sections

    # Henrik
    def get_abstract(self, query):
        sent_array = imp_sent_creator(self.full_text, query, 3)
        abstract = ""
        for sentence in sent_array:
            abstract += str(sentence.sent)
        return abstract

    # Jakob
    def inject_to_es(self):
        inject_one_file(self.get_json_object())

    def add_pages(self):
        json_tmp = json.loads(self.pdf_name.read())
        attr = str
        attr = (json_tmp["pages"])  # collect attribute

        index = 0
        for i in attr:
            self.sections.append([i, index])
            index += len(i)

