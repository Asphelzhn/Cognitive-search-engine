from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.core.files.storage import default_storage  # delete query
from django.db.models import F

"""
Oskar H
"""


class Document(models.Model):
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='detecht_api/static/pdf', max_length=100, blank=True)
    downloads = models.IntegerField(default=0)
    favorites = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title

    def delete(inputName):
        pdfToDelete = Document.objects.get(title=str(inputName))
        default_storage.delete(pdfToDelete.file.name)  # This part is deleting the pdf file from our storage.

        Document.objects.filter(title=str(inputName)).delete()  # This part is deleteting the row in db.
        return


class StagedPdf(models.Model):  # table for staged pdfs to be converted to Json format and added to elastic search
    pdf_name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    # id of each tuple is autogenerated


class StagedPdfTags(models.Model):
    staged_pdf_id = models.IntegerField()
    tag = models.CharField(max_length=200)


class Keywords(models.Model):
    word = models.CharField(max_length=20)  # High limit to avoid problems with creating keywords.

    # id of each tuple is autogenerated
    def __unicode__(self):
        return self.word

    def getKeywordId(word):
        return Keywords.objects.get(word=word).id


class Keyword_distance(models.Model):
    id_1 = models.PositiveIntegerField()  # Values from 0 to 2147483647
    id_2 = models.PositiveIntegerField()
    similarity = models.DecimalField(max_digits=5,
                                     decimal_places=4)  # Can take max 1 digit (0 or 1) and 4 decimals. eg 1.1234

    class Meta:
        unique_together = ("id_1", "id_2")  # Django doesn't support multiple pk, so this is the solution.

    def get_similarity(self):
        return self.similarity


class UserFavorites(models.Model):
    pdf_name = models.CharField(max_length=200)
    user_id = models.PositiveIntegerField()

    def add_favorite_pdf(user_id, pdf_name):
        UserFavorites.objects.get_or_create(user_id=user_id, pdf_name=pdf_name)
        return "Added favorite PDF"

    def remove_favorite_pdf(user_id, pdf_name):
        UserFavorites.objects.filter(user_id=user_id, pdf_name=pdf_name).delete()
        return "Removed favorite PDF"


class PDFImportance(models.Model):
    pdf_name = models.CharField(max_length=200)
    likes = models.PositiveIntegerField(default=0)
    downloads = models.PositiveIntegerField(default=0)
    custom_weight = models.DecimalField(default=0, max_digits=3, decimal_places=2)  # ex 0.99

    def update_likes(pdf_name):
        PDFImportance.objects.filter(pdf_name=pdf_name).update(likes=F('likes') + 1)
        return PDFImportance.objects.get(pdf_name=pdf_name).likes

    def update_downloads(pdf_name):
        PDFImportance.objects.filter(pdf_name=pdf_name).update(downloads=F('downloads') + 1)
        return PDFImportance.objects.get(pdf_name=pdf_name).downloads

    def update_weight(new_weight, pdf_name):
        PDFImportance.objects.filter(pdf_name=pdf_name).update(custom_weight=new_weight)
        return PDFImportance.objects.get(pdf_name=pdf_name).custom_weight

    def top_likes(x):
        like_list = PDFImportance.objects.order_by('-likes')[:x]
        return like_list

    def top_downloads(x):
        download_list = PDFImportance.objects.order_by('-downloads')[:x]
        return download_list




# Henrik
class Pdf_Name_Keyword_Weight(models.Model):
    pdf_name = models.TextField(max_length=50)
    keyword = models.TextField(max_length=50)
    weight = models.IntegerField()


class Pdf_Similarities(models.Model):
    document_name1 = models.TextField(max_length=50)
    document_name2 = models.TextField(max_length=50)
    similarity = models.FloatField()

#Henrik & Carl


class Interacted_documents(models.Model):

    down_prev = models.TextField(max_length=30)
    date = models.DateField()
    pdf_name = models.TextField(max_length=50)
    userid = models.TextField(max_length=20)

'''
Searches database
Edward & Severn
'''

class Searches_Database(models.Model):
    user_id = models.IntegerField(null=True)  # not mandatory, can be NULL
    search_date = models.DateTimeField(auto_now=False, auto_now_add=True)  # when the search was done
    search_query = models.CharField(max_length=50)  # RAW search_query
    standardized_search_query = models.CharField(max_length=50)  # standardization by using NLP spacy
    search_score = models.IntegerField(null=True, validators=[MinValueValidator(1),
 MaxValueValidator(10)])

    # add a new record into database
    def add_row(new_user_id, new_search_date, new_search_query, new_standardized_search_query, new_search_score):
        new_search = Searches_Database(user_id=new_user_id,
                                       search_date=new_search_date,
                                       search_query=new_search_query,
                                       standardized_search_query=new_standardized_search_query,
                                       search_score=new_search_score)
        new_search.save()


class User_Keyword(models.Model):
    userID = models.TextField(max_length=20)
    keyword = models.TextField(max_length=50)
