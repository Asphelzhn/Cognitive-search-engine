from django.contrib import admin

# Register your models here.
from .models import (StagedPdf, StagedPdfTags, Keywords, Keyword_distance, Pdf_Name_Keyword_Weight, Document, Interacted_documents)

admin.site.register(Keywords)
admin.site.register(Keyword_distance)
admin.site.register(Pdf_Name_Keyword_Weight)

admin.site.register(StagedPdf)
admin.site.register(StagedPdfTags)

admin.site.register(Document)
admin.site.register(Interacted_documents)