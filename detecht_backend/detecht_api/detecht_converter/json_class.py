import json


class json_class:
    pdf_name = ""
    tags = list()
    sections = list()
    keywords = list()


 j   def __init__(self, json):
        self.full_text = json

    #def insert_json(json):


    #def export_json():

     #   return json

    # Adds whole document to one string, can be a problem with memory management
    def add_full_text(self, fulltext):
        self.full_text = fulltext


    def get_full_text(self):
        return self.full_text


    def add_tag(tag):
        if tag not in tags:
            tags.append(tag)


    def remove_tag(tag):
        if tag in tags:
            tags.remove(tag)


    def get_tags():
        return tags


    def add_keyword(keyword):
        if keyword not in keywords:
            keywords.append(keyword)


    def remove_keyword(keyword):
        if keyword in keywords:
            keywords.remove(keyword)


    def get_keywords():
        return keywords


    def add_pdf_name(self,pdfname):
        self.pdf_name = pdfname


    def get_pdf_name(self):
        print("PdfName")
        return self.pdf_name


    #def add_section(start, end, section_tags):


    #def get_sections():


