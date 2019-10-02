from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.generic import TemplateView

# imports by ARMIN
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

# imports by OSKAR
from detecht_api.models import User
from detecht_api.models import Document #files
from rest_framework.views import APIView
#files
from.serializers import DocumentSerializer



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


class addPdf(APIView):

    def post(self, request): #json input "pdffile"
        if request.method == 'POST' and request.files['pdffile']:
            pdffile = request.files['pdffile']
            # models.FileField(upload_to='static/pdf')
            pdffile.save();  # Someware should "upload_to" be specified....
            return HttpResponse('{ "Result": "Done" }')

class profile(APIView):
    def post(self, request): #input {"id":"2"}
        # Test database
        #user = User(userName='hiden12345', firstName='Oskar', userID=5)
        #user.save()
        input= request.data
        query = User.objects.get(id=input["id"])
        #query = User.objects.all()    userName="hiden12345"
        name = query.firstName
        username = query.userName
        userid = str(query.userID)

        return HttpResponse('{ "Name": "' + name + '", "Poss": "' + username + '", "ID": "' + userid + '"  }')  # test


class updateProfile(APIView):
    def get(self, request):
        # get data from input data.

        # function updating data to userDB
        primaryKey = 1
        newName = "VilleJ"
        User.objects.filter(userID=primaryKey).update(firstName=newName)
        return HttpResponse('{ "Function": "done" }')  # later change

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
class UserTest(APIView):
   #permission_classes = (IsAuthenticated,)
   def post(self, request):
       #armin = User.objects.create(userName='armwa918', firstName='armin', userID=6)
       #query = User.objects.get(userName='armwa918')
       #name = query.firstName

       #OSkar put query to compare in database, email& PW gives sucess.

       
       return HttpResponse("Success")
   def post(self, request):
       if request.method == "POST":
           return HttpResponse({"Successful"})
       return HttpResponse({"Oops"})
# END: Code written by Armin


#files
class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer