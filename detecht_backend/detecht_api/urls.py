from django.conf.urls import url
from django.urls import path, include

from . import views
from rest_framework import routers


router = routers.DefaultRouter()

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^getcust/$', views.Customer.getCust),
    url(r'^apitest/$', views.CalcTest),
    url(r'^api/testget/$', views.TestGet),
    url(r'^api/addpdf/$', views.AddPdf),
    url(r'^api/search/$', views.Search),
    url(r'^api/getprofile/$', views.GetProfile),
    url(r'^api/updateprofile/$', views.UpdateProfile),
]
