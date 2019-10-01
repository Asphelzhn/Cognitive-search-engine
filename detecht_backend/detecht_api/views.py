from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.generic import TemplateView

# imports by ARMIN
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

# imports by OSKAR
from detecht_api.models import User
from rest_framework.views import APIView

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


@api_view(["POST"])
def Search(request):
    if request.method == 'GET':
        #Do search and get something.
        return HttpResponse('{ "Result": "A bunch of DATA" }') #later return data in correct format
    return HttpResponse('{ "Result": "Failed" }') #let the caller know the request failed. Somehow.


class profile(APIView):

    def get(self, request):
        query = User.objects.get(userName='hiden12345')
        name = query.firstName
        username = query.userName
        userid = str(query.userID)

        return HttpResponse('{ "Name": "' + name + '", "Poss": "' + username + '", "ID": "' + userid + '"  }')  # test


@api_view(["GET"]) #later POST
def UpdateProfile(requset):
    #get data from input data.
    #function updating data to userDB
    primaryKey=1
    newName="VilleJ"
    User.objects.filter(userID=primaryKey).update(firstName=newName)
    return HttpResponse('{ "Function": "done" }') #later change


class search(APIView):

    def post(self, request): #input: "searchString"
        input = request.data
        if input != None:
            # Do search and get something.

            name = input["searchString"]
            return HttpResponse('{ "Name": "' + name + '" }')  # test
            # return HttpResponse('{ "Result": "A bunch of DATA" }')
        return HttpResponse('{ "Result": "Failed" }')



# BEGIN: Code written by Armin
# Write Class-Based Views which helps keep code DRY.
class User(APIView):

    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {"message": "Hello World"}
        return HttpResponse(content)
# END: Code written by Armin

