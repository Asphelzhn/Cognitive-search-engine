import PyPDF2
import json
import re

# get the PDF path and read the file
file = "../static/pdf/BOAML_report_2016.pdf"
read_pdf = PyPDF2.PdfFileReader(file, strict=False)
all_pages = {}


# iterate the page numbers
for page in range(read_pdf.getNumPages()):
    data = read_pdf.getPage(page)
    #page_mode = read_pdf.getPageMode()
    page_text = data.extractText()
    modified_text = re.sub("\n","",page_text)
    all_pages[page] = modified_text

# create a JSON string from the dictionary
json_data = json.dumps(all_pages)
# print ("\nJSON:", json_data)


with open('test.json', 'w') as outfile:
    json.dump(all_pages, outfile)
