from pdfminer.converter import TextConverter
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser
import os
import io

#carl
#This method extracts one PDF at a time and outputs the scanned pages, along with the date created
def pdf_extractor(pdf_name):
    path = "detecht_api/static/pdf/"
    with os.scandir(path) as it:
        for entry in it:
            if entry.name.endswith(".pdf") and entry.is_file() and entry.name == pdf_name:

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

                device.close()
                retstr.close()

                parser = PDFParser(fp)
                doc = PDFDocument(parser)
                fp.close()
                date_created = doc.info[0]["CreationDate"]
                date_created = str(date_created[1:10])
                date_created = date_created[3:-1]
                date_created = date_created[0:4]+"-"+date_created[4:6]+"-"+date_created[5:7]

    return pages, date_created