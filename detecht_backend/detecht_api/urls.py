from django.conf.urls import url
from django.urls import path, include

#adminsite
from django.contrib import admin
from django.urls import path

from . import views
from rest_framework import routers

# files
from .views import DocumentViewSet

router = routers.DefaultRouter()

# files
router.register(r'files', DocumentViewSet)

urlpatterns = [
    path('admin_db/', admin.site.urls),
    url(r'^$', views.HomePageView.as_view()),
    url(r'^admin/', views.HomePageView.as_view()),
    url(r'^search/', views.HomePageView.as_view()),
    url(r'^saved/', views.HomePageView.as_view()),
    url(r'^upload/', views.HomePageView.as_view()),
    url(r'^api/addfile/$', views.AddFile.as_view()),
    url(r'^api/search/$', views.Search.as_view()),
    url(r'^api/', include(router.urls)), #files
    url(r'^api/deletepdf/$', views.DeletePdf.as_view()),#deletePDF
    url(r'^api/pdftoes/$', views.AddPdfsToES.as_view()),#Call to add all staged pdfs to Elastic search
    url(r'^api/getanalytics/$', views.GetAnalytics.as_view()),
    url(r'^api/getabstract/$', views.GetAbstract.as_view()),
    url(r'^api/getautocomplete/$', views.GetAutoComplete.as_view()),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^api/interactwithdocument/$', views.InteractWithDocument.as_view()),
    url(r'^api/trendingdocuments/$', views.TrendingDocuments.as_view()),
    url(r'^api/userfavorite/$', views.UserFavorite.as_view()),
    url(r'^api/getuserfavorites/$', views.GetLikedDocs.as_view()),
    url(r'^api/getdoc/$', views.GetDoc.as_view()),
    url(r'^api/relateddocuments/$', views.RelatedDocuments.as_view()),
    url(r'^api/isfavorite/$', views.IsFavorite.as_view())


]
