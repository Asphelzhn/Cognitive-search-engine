from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic import TemplateView

from detecht_api.detecht_db_handling.keyword import Preview_Document

"""
Oskar H & Armin
"""

# imports by ARMIN
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from detecht_api.models import Keywords, PDFImportance, UserFavorites, Keyword_distance

# imports by OSKAR
from detecht_api.models import Document #files
from rest_framework.views import APIView
from.serializers import DocumentSerializer

# Create your views here.
from rest_framework import status, viewsets, serializers

# Our packages
from detecht_api.detecht_es import search, insert_file
from detecht_api.detecht_db_handling.staged_pdf import insert_all_staged_pdf_into_es, add_staged_pdf
from detecht_api.detecht_db_handling.analytics import get_analytics_document
from detecht_api.detecht_nlp.spell_check import spell_check

from detecht_api.detecht_db_handling import get_autocomplete

class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)


# class Profile(APIView):
#     def post(self, request): #input {"id":"2"}
#         # Test database
#         #user = User(userName='hiden12345', firstName='Oskar', userID=5)
#         #user.save()
#         input= request.data
#         query = User.objects.get(id=input["id"])
#         #query = User.objects.all()    userName="hiden12345"
#         name = query.firstName
#         username = query.userName
#         userid = str(query.userID)
#
#         return HttpResponse('{ "Name": "' + name + '", "Poss": "' + username + '", "ID": "' + userid + '"  }')  # test


# class UpdateProfile(APIView):
#     def get(self, request):
#         # get data from input data.
#
#         # function updating data to userDB
#         primaryKey = 1
#         newName = "VilleJ"
#         User.objects.filter(userID=primaryKey).update(firstName=newName)
#         return HttpResponse('{ "Function": "done" }')  # later change


class Search(APIView):
    def post(self, request): #input: "searchString"
        response = {
            'success': False,
            'totalResult': 0,
            'content': [],
            'spellcheck': []
        }
        input = request.data
        if input != {}:
            query = input["query"]
            res = search.search(query, 10)
            response['success'] = True
            words = query.split()
            for word in words:
                response['spellcheck'].append({'word': word, 'spellcheck': sorted(spell_check.candidates(word))})
            response['totalResult'] = res['hits']
            content = res['results']
            for c in content:
                response['content'].append(c.frontend_result(query))
            return JsonResponse(response)  # test
        return JsonResponse(response)


class GetAbstract(APIView):
    def post(self, request): #input: "searchString"
        response = {
            'success': False,
            'abstracts': []
        }
        input = request.data["networkAbstractRequest"]
        if input != {}:
            pdf = input["pdf"]
            query = input["query"]
            res = search.get_pdf(pdf)
            response['success'] = True
            response['abstracts'] = res['j_class'].get_abstract(query)
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
            add_staged_pdf(file_name, title)
            # Old code inserting file into Elstic Search.
            # json_string = '{"title":"' + title + '", "fileName":"' + file_name + '"}'
            #
            # insert_file.inject_one_file(json_string)
            response['success'] = True
            return JsonResponse(response)
        return JsonResponse(response)


# BEGIN: Code written by Armin
class Keyword(APIView):
   # permission_classes = (IsAuthenticated,)
   def post(self, request): #input: "keyword"
        input = request.data

        wordToStore = input["keyword"]
        message = Keywords.add_keyword(wordToStore)

        return HttpResponse(message)

#class KeywordSimilarity(APIView):

#    def post(self, request): #input: keyword1, keyword2, similarity
        #input = request.data
        #message = UserFavorites.add_favorite_pdf(1, input["favoritepdf"])
        #input = request
        #test = UserFavorites.objects.filter(user_id=1, pdf_name="hej")
        #UserFavorites.remove_favorite_pdf(1, "hej")
        #message = UserFavorites.objects.get(user_id=1, pdf_name="hej").pdf_name
 #       return HttpResponse(message)

# END: Code written by Armin

# files
class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

#delete pdf
class DeletePdf(APIView):
    def post(self, request):
        response = {
            'success': False
        }

        inputfile = request.data

        if inputfile !={}:
            insert_file.delete_from_index(inputfile["title"])
            Document.delete(inputfile["title"]) #runs a function in models that deletes our pdf.
            response['success'] = True
        return JsonResponse(response)


class AddPdfsToES(APIView):
    def put(self, request):
        insert_all_staged_pdf_into_es()
        response = {
            'success': True
        }
        return JsonResponse(response)


class GetAnalytics(APIView):
    def get(self, request):
        response = get_analytics_document()
        return JsonResponse(response)


class InteractWithDocument(APIView):
    def post(self, request):
        data_in = request.data
        Preview_Document(pdf_name=data_in["pdf_name"], userid=data_in["user_id"], type = data_in["type"])
        return


class GetAutoComplete(APIView):
    def post(self, request):
        response = {
            'success': False,
            'autocomplete': []
        }
        input = request.data
        if input != {}:
            query = input["query"]
            response['success'] = True
            response['autocomplete'] = get_autocomplete.get_autocomplete(query)
            return JsonResponse(response)
        return JsonResponse(response)
