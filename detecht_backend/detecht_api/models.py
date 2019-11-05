from django.db import models
from django.core.files.storage import default_storage #delete query
from django.db.models import F

"""
Oskar H
"""


class User(models.Model):
    userName = models.TextField(max_length=50)
    firstName = models.TextField(max_length=50)


class Document(models.Model):
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='detecht_api/static/pdf', max_length=100, blank=True)

    def __unicode__(self):
        return self.title
    
    def delete(inputName):
        pdfToDelete = Document.objects.get(title = str(inputName))
        default_storage.delete(pdfToDelete.file.name) #This part is deleting the pdf file from our storage.

        Document.objects.filter(title = str(inputName)).delete() #This part is deleteting the row in db.
        return
# end Oskar


class Keywords(models.Model):
    word = models.CharField(max_length=20)  #High limit to avoid problems with creating keywords.
    #id of each tuple is autogenerated

    def __unicode__(self):
        return self.word

    def add_keyword(word):
        keyword, created = Keywords.objects.get_or_create(word=word)
        if created:
            keyword.save()
            return "Keyword " + keyword.word + " saved"
        return "Already in db"


class Keyword_distance(models.Model):
    id_1 = models.PositiveIntegerField()    # Values from 0 to 2147483647
    id_2 = models.PositiveIntegerField()
    similarity = models.DecimalField(max_digits=5, decimal_places=4) #Can take max 1 digit (0 or 1) and 4 decimals. eg 1.1234

    class Meta:
        unique_together = ("id_1", "id_2") #Django doesn't support multiple pk, so this is the solution.

    def add_keyword_distance(id1, id2, similarity):
        keyword_distance, created = Keyword_distance.objects.get_or_create(id_1=id1, id_2=id2, similarity=similarity)
        if created:
            return "Keyword distance " + keyword_distance.id_1 + keyword_distance.id_2 + keyword_distance.similarity \
                   + "created"
        return "Keyword distance already in db"

    def get_similarity(self):
        return self.similarity


class PDFImportance(models.Model):
    pdf_name = models.CharField(max_length=200)
    likes = models.PositiveIntegerField(default=0)
    downloads = models.PositiveIntegerField(default=0)
    custom_weight = models.DecimalField(default=0, max_digits=3, decimal_places=2) #ex 0.99

    def update_likes(self, pdf_name):
        PDFImportance.objects.filter(pdf_name=pdf_name).update(likes=F('likes')+1)
        return PDFImportance.objects.get(pdf_name=pdf_name).likes

    def update_downloads(self, pdf_name):
        PDFImportance.objects.filter(pdf_name=pdf_name).update(downloads=F('downloads')+1)
        return PDFImportance.objects.get(pdf_name=pdf_name).downloads

    def update_weight(self, new_weight, pdf_name):
        PDFImportance.objects.filter(pdf_name=pdf_name).update(custom_weight=new_weight)
        return PDFImportance.objects.get(pdf_name=pdf_name).custom_weight




