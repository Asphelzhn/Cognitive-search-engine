from detecht_api.models import Document
from django.db.models import Sum


def get_analytics_document():
    nr_of_documents = Document.objects.count()
    nr_of_downloads = Document.objects.all().aggregate(Sum('downloads'))
    nr_of_favorites = Document.objects.all().aggregate(Sum('favorites'))
    res = {
        'documents': nr_of_documents,
        'downloads': nr_of_downloads['downloads__sum'],
        'favorites': nr_of_favorites['favorites__sum']
    }
    return res


def get_downloads(pdf_name):
    doc = Document.objects.get(title=pdf_name)
    return doc.downloads


def get_favorites(pdf_name):
    doc = Document.objects.get(title=pdf_name)
    return doc.favorites
