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
    url(r'^getcust/$', views.Customer.getCust),
    url(r'^apitest/$', views.CalcTest),
    url(r'^api/testget/$', views.TestGet),
    url(r'^api/addpdf/$', views.addPdf.as_view()),
    url(r'^api/search/$', views.search.as_view()),
    url(r'^api/profile/$', views.profile.as_view()),
    url(r'^api/updateprofile/$', views.updateProfile.as_view()),
    url(r'^api/user/$', views.UserTest.as_view()),
    url(r'^api/', include(router.urls)), #files
]
