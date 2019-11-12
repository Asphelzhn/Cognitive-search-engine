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
    url(r'^upload/', views.HomePageView.as_view()),
    url(r'^api/addfile/$', views.AddFile.as_view()),
    url(r'^api/search/$', views.Search.as_view()),
    url(r'^api/', include(router.urls)), #files
    url(r'^api/deletepdf/$', views.DeletePdf.as_view()),#deletePDF
    url(r'^api/pdftoes/$', views.AddPdfsToES.as_view()),#Call to add all staged pdfs to Elastic search
    url(r'^api/getanalytics/$', views.GetAnalytics.as_view()),
    url(r'^api/getabstract/$', views.GetAbstract.as_view())


]
