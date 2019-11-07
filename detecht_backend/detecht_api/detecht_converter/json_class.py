import json

from detecht_api.detecht_converter.plain_text import json_to_plaintext
from detecht_api.detecht_converter.section_class import *
from detecht_api.detecht_converter.keyword_class import *
from detecht_api.detecht_nlp import imp_sent_creator
from detecht_api.detecht_es.insert_file import inject_one_file
from detecht_api.detecht_nlp.keywordExtraction.yake_api import Yake4Keyword


# Jakob, Carl and Oscar


class json_class:
    pdf_name = ""
    full_text = ""
    title = ""
    tags = list()
    sections = list()
    keywords = list()

    def __init__(self, json_file):
        json_doc = json.loads(json_file)
        self.add_full_text(json_doc["full_text"])
        self.set_pdf_name(json_doc["pdf_name"])
        self.add_title(json_doc["title"])
        for keyword in json_doc["keywords"]:
            self.keywords.append(keyword_class(keyword["keyword"], keyword["weight"]))
        for tag in json_doc["tags"]:
            self.add_tag(tag)
        for section in json_doc["sections"]:
            self.add_section(section["start"], section["end"], section["section_keyword"])

    def __init__(self, pdf_name, title, tags):
        x = convert_pdf_to_json(pdf_name)  # convert_pdf_to_json not yet working
        y = json_to_plaintext(x)
        self.add_full_text(y)

        self.set_pdf_name(pdf_name)
        self.add_tag(title)

        keywords_list = Yake4Keyword.yake_api(self.full_text, pdf_name)
        self.add_keyword(keywords_list)

        for tag in tags:
            self.add_tag(tag)

        text_len = len(self.full_text)
        i = 0
        while i < text_len:
            section_length = 3000
            if (i + section_length) < text_len:
                while (self.full_text[i] != ("." or "!" or "?")) and (i < text_len):
                    section_length += 1
                # generate keywords here
                # self.add_section(i, i+section_length, keywords)
                i += section_length

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
        inject_one_file(get_json_object())
