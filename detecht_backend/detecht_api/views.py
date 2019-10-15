from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.generic import TemplateView

"""
Oskar H & Armin
"""

# imports by ARMIN
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from detecht_api.models import Keywords
from detecht_api.models import Keyword_distance

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


# Our packages
from detecht_api.detecht_es import search, insert_file


class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)


# class PdfUpload(APIView):
#     def post(self, request): #json input "pdffile"
#         if request.method == 'POST' and request.files['pdffile']:
#             pdf_file = request.files['pdffile'] # TODO ask Oskar
#             models.FileField(upload_to='static/pdf')
#             pdf_file.save();  # Someware should "upload_to" be specified....
#             return HttpResponse('{ "success": "true" }')
#         return HttpResponse('{ "success": "false" }')


class Profile(APIView):
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


class UpdateProfile(APIView):
    def get(self, request):
        # get data from input data.

        # function updating data to userDB
        primaryKey = 1
        newName = "VilleJ"
        User.objects.filter(userID=primaryKey).update(firstName=newName)
        return HttpResponse('{ "Function": "done" }')  # later change


class Search(APIView):
    def post(self, request): #input: "searchString"
        response = {
            'success': False,
            'totalResult': 0,
            'content': []
        }
        input = request.data
        if input != {}:
            query = input["query"]
            res = search.search(query, 10)
            response['success'] = True
            response['totalResult'] = res['hits']['total']['value']
            content = res['hits']['hits']
            for c in content:
                response['content'].append({'pdfTitle': c['_source']['title'], 'pdfName': c['_source']['fileName']})
            return JsonResponse(response)  # test
        return JsonResponse(response)


class AddFile(APIView):
    def post(self, request): #input: response from api/files/
        response = {
            'success': False
        }
        input = request.data
        if input != {}:
            input = input["data"]
            title = input["title"]
            file_name = input["file"].split('static/pdf/')[-1]
            json_string = '{"title":"' + title + '", "fileName":"' + file_name + '"}'

            insert_file.inject_one_file(json_string)
            response['success'] = True
            return JsonResponse(response)
        return JsonResponse(response)


# BEGIN: Code written by Armin
# Write Class-Based Views which helps keep code DRY.
class Keyword(APIView):
   # permission_classes = (IsAuthenticated,)
   def post(self, request): #input: "keyword"

        input = request.data

        wordToStore = input["keyword"]
        message = Keywords.add_keyword(wordToStore)
        #message2 = Keywords.add_keyword("banan")

    #message = Keyword_distance.add_keyword_distance(test, id1=Keywords.objects.get(word="banan").id, id2=Keywords.objects.get(word="apa").id, similarity=1.0000)
    #message = Keyword_distance.objects.get(id=1)
        return HttpResponse(message)

# END: Code written by Armin

# files
class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

