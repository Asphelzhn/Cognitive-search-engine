import PyPDF2
import json
from os import listdir
from os.path import isfile, join

# get the PDF path and read the file
file = "BOAML_report_2017.pdf"
read_pdf = PyPDF2.PdfFileReader(file, strict=False)

# get the read object's meta info
pdf_meta = read_pdf.getDocumentInfo()
all_pages = {}
all_pages["meta"] = {}

for meta, value in pdf_meta.items():
    all_pages["meta"][meta] = value

# iterate the page numbers
for page in range(read_pdf.getNumPages()):
    data = read_pdf.getPage(page)
    page_mode = read_pdf.getPageMode()
    page_text = data.extractText()
    all_pages[page] = page_text


# create a JSON string from the dictionary
json_data = json.dumps(all_pages)
# print ("\nJSON:", json_data)


with open('test.json', 'w') as outfile:
    json.dump(all_pages, outfile)
