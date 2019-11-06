import PyPDF2
import json
import os
import re

def convert_pdf_to_json():

    # get all PDFs  in the path
    path = "detecht_api/static/pdf"
    with os.scandir(path) as it:
        for entry in it:
            if entry.name.endswith(".pdf") and entry.is_file():
                print("Currently scanning: " + entry.name)
                file = entry.path

                # read the current pdf
                read_pdf = PyPDF2.PdfFileReader(file, strict=False)
                all_pages = {}

                # iterate all pages
                all_text = ""
                for page in range(read_pdf.getNumPages()):
                    data = read_pdf.getPage(page)
                    page_text = data.extractText()
                    modified_text = re.sub("\n", "", page_text)
                    all_text = all_text + modified_text

                all_pages["All_text"] = all_text

                # creates a JSON file
                filename = entry.name
                filename = filename[:-4]
                filepath = 'detecht_api/static/json/' + filename + '.json'
                with open(filepath,'w+') as outfile:
                    json.dump(all_pages, outfile)



