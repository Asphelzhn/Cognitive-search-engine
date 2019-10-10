import json
from section_class import *
from keyword_class import *

# Jakob & Carl
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
        self.add_pdf_name(json_doc["pdf_name"])
        self.add_title(json_doc["title"])
        for keyword in json_doc["keywords"]:
            self.keywords.append(keyword_class(keyword["keyword"],keyword["weight"]))
        for tag in json_doc["tags"]:
            self.add_tag(tag)
        for section in json_doc["sections"]:
            self.add_section(section["start"],section["end"],section["section_keyword"])
            #section_tmp = section_class(section["start"],section["end"])
            #for keyword in section["section_keyword"]:
            #   section_tmp.add_keyword(keyword["keyword"],keyword["weight"])
            #self.sections.append(section_tmp)





    def export_json(self,file_name=""):
        if file_name == "":
            file_name = self.pdf_name
        keywords_tmp=list()
        for keyword_tmp in self.keywords:
            keywords_tmp.append(keyword_tmp.get_keyword_dict())
        sections_tmp=list()
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
            tags.remove(tag)


    def get_tags():
        return tags


    def add_keyword(self, keyword):
        if keyword not in self.keywords:
            self.keywords.append(keyword)


    def remove_keyword(keyword):
        if keyword in keywords:
            keywords.remove(keyword)


    def get_keywords():
        return keywords


    def add_pdf_name(self,pdfname):
        self.pdf_name = pdfname


    def get_pdf_name(self):
        return self.pdf_name

    #
    def add_section(self, start, end, section_keywords):
        if start < end:
            section_tmp = section_class(start,end)
            for keyword in section_keywords:
                section_tmp.add_keyword(keyword["keyword"],keyword["weight"])
            self.sections.append(section_tmp)
        else:
            print("hoppsan")
            raise ValueError('End index can not be lower than start index.')



    def get_sections():
        return sections


