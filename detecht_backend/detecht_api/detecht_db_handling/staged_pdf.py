from detecht_api.models import StagedPdf
from detecht_api.models import StagedPdfTags



def add_staged_pdf(pdf_name, title):
    new_pdf = StagedPdf(pdf_name=pdf_name, title=title)
    new_pdf.save()
    return


def remove_staged_pdf(title):
    try:
        StagedPdf.objects.filter(title=title).delete()
    except:
        return False #returns false if no object is deleted.
    return True #returns true if object is removed successfully.


def add_staged_pdf_tag(staged_pdf_id, tag):
    new_tag = StagedPdfTags(staged_pdf_id=staged_pdf_id, tag=tag)
    new_tag.save()
    return


def remove_staged_pdf_tag(staged_pdf_id, tag):
    try:
        StagedPdfTags.objects.filter(staged_pdf_id=staged_pdf_id, tag=tag)
    except:
        return False #returns false if no object is deleted
    return True #returns true if object is removed successfully
