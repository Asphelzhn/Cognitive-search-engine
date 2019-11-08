from detecht_api.models import Document

def get_analytics_document():
    nr_of_documents = Document.objects.count()
    nr_of_downloads = Document.objects.all().aggregate(sum('downloads'))
    nr_of_favorites = Document.objects.all().aggregate(sum('favorites'))
    res = {
        'documents' : nr_of_documents,
        'downloads' : nr_of_downloads,
        'favorites' : nr_of_favorites
    }
    return res