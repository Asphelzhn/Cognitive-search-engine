from django.db import models
from django.core.files.storage import default_storage #delete query
"""
Oskar H
"""

# By Oskar H
class User(models.Model):
    userID = models.IntegerField() #could be removed since and id automaticly is generated. the id starts from 1 and is incrementing for each new tuple.
    userName = models.TextField(max_length=50)
    firstName = models.TextField(max_length=50)


# files
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
