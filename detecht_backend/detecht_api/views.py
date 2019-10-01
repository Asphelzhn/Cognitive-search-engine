from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.generic import TemplateView

# imports by ARMIN
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

# imports by OSKAR
# from django.db import models ----

# Create your views here.
from rest_framework import status, viewsets, serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.utils import json


class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)


class Customer(TemplateView):
    def getCust(request):
        name = 'Nicklas'
        return HttpResponse('{ "name":"' + name + '", "age":22, "city":"Linkoping" }')


@api_view(["POST"])
def CalcTest(x1):
    try:
        x = json.loads(x1.body)
        y = str(x * 100)
        return JsonResponse("Result:" + y, safe=False)
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def TestGet(x1):
    try:
        x = 10
        y = str(x * 100)
        return JsonResponse("Result:" + y, safe=False)
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)


@api_view(["GET, POST"])  # later POST, not done.
def AddPdf(request):
    if request.method == 'POST' and request.files['pdffile']:
        pdffile = request.files['pdffile']
        # models.FileField(upload_to='static/pdf')
        pdffile.save();  # Someware should "upload_to" be specified....
        return HttpResponse('{ "Result": "Done" }')


@api_view(["GET"])
def Search(request):
    if request.method == 'GET':
        #Do search and get something.
        return HttpResponse('{ "Result": "A bunch of DATA" }') #later return data in correct format
    return HttpResponse('{ "Result": "Failed" }') #let the caller know the request failed. Somehow.

@api_view(["GET"])
def GetProfile(userID):
    #function getting the data from userDB
    name = "oskar"
    poss = "B-dev"
    return HttpResponse('{ "Name": "' + name + '", "Poss": "' + poss + '" }') #test

@api_view(["POST"])
def UpdateProfile(requset):
    #get data from input data.
    #function updating data to userDB
    return HttpResponse('{ "Function": "done" }') #later change

@api_view(["POST"])
def Search(input):
    if input != None:
        # Do search and get something.
        return HttpResponse('{ "Result": "A bunch of DATA" }')
    return HttpResponse('{ "Result": "Failed" }')


# BEGIN: Code written by Armin
# Write Class-Based Views which helps keep code DRY.
class User(APIView):

    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {"message": "Hello World"}
        return HttpResponse(content)
# END: Code written by Armin

