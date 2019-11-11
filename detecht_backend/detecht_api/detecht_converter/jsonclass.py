import json

from detecht_api.detecht_converter.plain_text import json_to_plaintext
from detecht_api.detecht_converter.section_class import *
from detecht_api.detecht_converter.keyword_class import *
from detecht_api.detecht_nlp import imp_sent_creator
from detecht_api.detecht_es.insert_file import inject_one_file
from detecht_api.detecht_nlp.keywordExtraction.yake_api import Yake4Keyword
from detecht_api.detecht_converter.pdf_converter import pdf_to_json


# Jakob, Carl and Oscar


class JsonClass:

    def __init__(self, pdf_name, title, full_text):
        self.pdf_name = pdf_name
        self.full_text = title
        self.title = full_text
        self.tags = list()
        self.sections = list()
        self.keywords = list()

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
        full_text = pdf_to_json(pdf_name)  # convert_pdf_to_json not yet working
        # y = json_to_plaintext(x)
        json_obj = cls(pdf_name, title, full_text)

        keywords_list = Yake4Keyword.yake_api(json_obj.full_text, pdf_name)
        for keyword in keywords_list:
            # TODO add keywords to db
            json_obj.add_keyword(keyword[0], keyword[1])

        for tag in tags:
            json_obj.add_tag(tag)

        return json_obj

        text_len = len(json_obj.full_text)
        i = 0
        while i < text_len:
            section_length = 3000
            if (i + section_length) < text_len:
                while (json_obj.full_text[i] != ("." or "!" or "?")) and (i < text_len):
                    section_length += 1
                # generate keywords here
                # self.add_section(i, i+section_length, keywords)
                i += section_length

    def frontend_result(self):
        return {'pdfTitle': self.title, 'pdfName': self.pdf_name}

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
            'full_text': self.full_text}
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
    def add_full_text(self, fulltext):
        self.full_text = fulltext

    def get_full_text(self):
        return self.full_text

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
