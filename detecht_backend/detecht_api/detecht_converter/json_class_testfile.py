from json_class import *

json = json_class("hej")
json.add_pdf_name("pdf.pdf")
print(json.get_full_text())
print(json.get_pdf_name())