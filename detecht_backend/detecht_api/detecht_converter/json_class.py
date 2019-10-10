import json
#from section_class import *
#from keyword_class import *
# Jakob & Carl
class json_class:
    pdf_name = ""
    tags = list()
    sections = ()
    section_class()
    keyword = keyword_class()


    def __init__(self, json_file):
        json_doc = json.loads(json_file)
        self.add_full_text(json_doc["full_text"])
        self.add_pdf_name(json_doc["pdf_name"])
        for keyword in json_doc["keywords"]:
            self.add_keyword(keyword)
        for tag in json_doc["tags"]:
            self.add_tag(tag)
        print(json_doc["sections"])
        for section in json_doc["sections"]

        #self.add_keyword()
        #self.add_section()
        #self.add_tag()




    #def export_json():

     #   return json

    # Adds whole document to one string, can be a problem with memory management
    def add_full_text(self, fulltext):
        self.full_text = fulltext


    def get_full_text(self):
        return self.full_text


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


    def add_section(start, end, section_tags):
        sections.append[start, end, section_tags]


    def get_sections():
        return sections


