from detecht_api.models import StagedPdf
from detecht_api.models import StagedPdfTags
from detecht_api.detecht_converter.jsonclass import JsonClass
# Import commented since it is not used in file and tests are complaining about it but i dont want to remove it
# completely //Jakob
# from detecht_api.detecht_es import insert_file

def add_staged_pdf(pdf_name, title):
    new_pdf = StagedPdf(pdf_name=pdf_name, title=title)
    new_pdf.save()
    return


def remove_staged_pdf(title):
    try:
        StagedPdf.objects.filter(title=title).delete()
    except Exception:
        return False  # returns false if no object is deleted.
    return True  # returns true if object is removed successfully.


def add_staged_pdf_tag(staged_pdf_id, tag):
    new_tag = StagedPdfTags(staged_pdf_id=staged_pdf_id, tag=tag)
    new_tag.save()
    return


def remove_staged_pdf_tag(staged_pdf_id, tag):
    try:
        StagedPdfTags.objects.filter(staged_pdf_id=staged_pdf_id, tag=tag)
    except Exception:
        return False  # returns false if no object is deleted
    return True  # returns true if object is removed successfully


def insert_all_staged_pdf_into_es():
    all_pdfs = StagedPdf.objects.all()

    for a in all_pdfs:
        json_obj = JsonClass.init_from_pdf(a.pdf_name, a.title, [])
        json_obj.inject_to_es()
        # json_string = '{"title":"' + a.title + '", "fileName":"' + a.pdf_name + '"}'
        # insert_file.inject_one_file(json_string)
        remove_staged_pdf(a.title)
    return
