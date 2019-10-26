from django.conf.urls import url
from django.urls import path, include

from . import views
from rest_framework import routers
"""
Oskar H & Armin
"""
# files
# from rest_framework.routers import DefaultRouter
from .views import DocumentViewSet

router = routers.DefaultRouter()

# files
router.register(r'files', DocumentViewSet)

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^admin/', views.HomePageView.as_view()),
    url(r'^upload/', views.HomePageView.as_view()),
    # url(r'^api/pdfupload/$', views.PdfUpload.as_view()),
    url(r'^api/addfile/$', views.AddFile.as_view()),
    url(r'^api/search/$', views.Search.as_view()),
    url(r'^api/profile/$', views.Profile.as_view()),
    url(r'^api/updateprofile/$', views.UpdateProfile.as_view()),
    url(r'^api/keyword/$', views.Keyword.as_view()),
    url(r'^api/keywordsimilarity/$', views.KeywordSimilarity.as_view()),
    url(r'^api/', include(router.urls)), #files
    url(r'^api/deletepdf/$', views.DeletePdf.as_view()),#deletePDF

]
