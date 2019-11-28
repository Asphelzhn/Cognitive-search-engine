from detecht_api.models import Document, UserFavorites
from django.db.models import F


def update_favorites(pdf_name):
    Document.objects.filter(file=pdf_name).update(favorites=F('favorites') + 1)
    return


def update_downloads(pdf_name):
    Document.objects.filter(file=pdf_name).update(downloads=F('downloads') + 1)
    return


def update_weight(new_weight, pdf_name):
    Document.objects.filter(file=pdf_name).update(custom_weight=new_weight)
    return


def add_favorite_pdf(user_id, pdf_name):
    UserFavorites.objects.get_or_create(user_id=user_id, pdf_name=pdf_name)
    return


def remove_favorite_pdf(user_id, pdf_name):
    UserFavorites.objects.filter(user_id=user_id, pdf_name=pdf_name).delete()
    return
