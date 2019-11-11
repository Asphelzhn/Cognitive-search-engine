from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.core.files.storage import default_storage  # delete query


class User(models.Model):
    userID = models.IntegerField()  # could be removed since and id automaticly is generated. the id starts from 1 and is incrementing for each new tuple.
    userName = models.TextField(max_length=50)
    firstName = models.TextField(max_length=50)


class Document(models.Model):
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='detecht_api/static/pdf', max_length=100, blank=True)

    def __unicode__(self):
        return self.title

    def delete(inputName):
        pdfToDelete = Document.objects.get(title=str(inputName))
        default_storage.delete(pdfToDelete.file.name)  # This part is deleting the pdf file from our storage.

        Document.objects.filter(title=str(inputName)).delete()  # This part is deleteting the row in db.
        return


# table for staged pdfs to be converted to Json format and added to elastic search
class StagedPdf(models.Model):
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

    def add_keyword(word):
        keyword, created = Keywords.objects.get_or_create(word=word)
        if created:
            keyword.save()
            return True
        return False


class Keyword_distance(models.Model):
    id_1 = models.IntegerField()  # Values from -2147483648 to 2147483647
    id_2 = models.IntegerField()
    similarity = models.DecimalField(max_digits=5,
                                     decimal_places=4)  # Can take max 1 digit (0 or 1) and 4 decimals. eg 1.1234

    class Meta:
        unique_together = ("id_1", "id_2")  # Django doesn't support multiple pk, so this is the solution.

    def add_keyword_distance(id1, id2, similarity):
        keyword_distance, created = Keyword_distance.objects.get_or_create(id_1=id1, id_2=id2, similarity=similarity)
        if created:
            return "Keyword distance " + keyword_distance.id_1 + keyword_distance.id_2 + keyword_distance.similarity \
                   + "created"
        return "Keyword distance already in db"

    def get_similarity(self):
        return self.similarity


# Henrik


class Pdf_Name_Keyword_Weight(models.Model):

    pdf_name = models.TextField(max_length=50)
    # keyword = ArrayField(models.TextField(max_length=50))  # if we want several keywords for every object
    # possible if PostgreSQL is used to build the database.
    keyword = models.TextField(max_length=50)
    weight = models.IntegerField()

    def add_row(pdf, keys, weight1):
        new = Pdf_Name_Keyword_Weight(pdf_name=pdf, keyword=keys, weight=weight1)
        new.save()

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

