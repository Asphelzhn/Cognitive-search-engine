from detecht_api.models import Document
from django.db.models import F


def update_likes(pdf_name):
    Document.objects.filter(pdf_name=pdf_name).update(favorites=F('favorites') + 1)
    return


def update_downloads(pdf_name):
    Document.objects.filter(pdf_name=pdf_name).update(downloads=F('downloads') + 1)
    return


def update_weight(new_weight, pdf_name):
    Document.objects.filter(pdf_name=pdf_name).update(custom_weight=new_weight)
    return