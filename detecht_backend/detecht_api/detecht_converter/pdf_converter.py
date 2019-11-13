from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
import os
import io

def convert_pdf_to_json():
    path = "detecht_api/static/pdf/"
    with os.scandir(path) as it:
        for entry in it:
            if entry.name.endswith(".pdf") and entry.is_file():


                fp = open(path + entry.name, 'rb')

                # Iterate over the pages
                pages = []
                for page in PDFPage.get_pages(fp):
                    rsrcmgr = PDFResourceManager()
                    retstr = io.StringIO()
                    device = TextConverter(rsrcmgr, retstr)
                    interpreter = PDFPageInterpreter(rsrcmgr, device)


                    interpreter.process_page(page)
                    pagetext = retstr.getvalue()
                    pagetext = pagetext[:-1]
                    pages.append(pagetext)
                    retstr.close()

                #text = retstr.getvalue()

                fp.close()
                device.close()
                retstr.close()
                all_text = ""
                for i in pages:
                    all_text += i
                # print the text to file
                filename = entry.name
                filename = filename[:-4]
                filepath = 'detecht_api/static/json/' + filename + '.json'
                with open(filepath, 'w+', encoding="utf-8") as f:
                    print("{\"All_text\": \"" + all_text + "\",", file=f)
                    print("\"pages\":[", end="",file=f)
                    for i in range(len(pages)-1):
                        print(" \""+pages[i]+"\",", end="",file=f)
                    print(" \""+pages[-1]+"\" ",end="",file=f)
                    print("]",end="",file=f)
                    print("}",end="",file=f)
