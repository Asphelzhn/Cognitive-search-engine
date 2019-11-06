import PyPDF2
import json
import os
import re
import unicodedata

#Titta på textract som alternativ
def convert_pdf_to_json():

    # get the PDF path and read the file
    file = 'detecht_api/static/pdf/BOAML_report_2016.pdf'

    #file = open(file, "r")
    read_pdf = PyPDF2.PdfFileReader(file, strict=False)
    all_pages = {}
    #file.close()

    # iterate the page numbers
    for page in range(read_pdf.getNumPages()):
        data = read_pdf.getPage(page)
        #page_mode = read_pdf.getPageMode()
        page_text = data.extractText()

        modified_text = re.sub(" \n", "", page_text)
        #modified_text = re.sub("\n","",page_text)

        #modified_text = re.compile(modified_text, re.UNICODE)
        #all_pages[page] = modified_text
        all_pages[page] = modified_text

    # create a JSON string from the dictionary
    json_data = json.dumps(all_pages)
    with open('BOAML_report_2016.json', 'w+') as outfile:
        json.dump(all_pages, outfile)



