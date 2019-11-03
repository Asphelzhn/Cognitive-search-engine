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


# table for staged pdfs to be converted to Json fromat and added to elastic search
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

    def get_similarity(self):
        return self.similarity
