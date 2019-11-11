from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic import TemplateView

# imports by OSKAR
from detecht_api.models import Document #files
from rest_framework.views import APIView
from.serializers import DocumentSerializer

# Create your views here.
from rest_framework import status, viewsets, serializers

# Our packages
from detecht_api.detecht_es import search, insert_file
from detecht_api.detecht_db_handling.staged_pdf import insert_all_staged_pdf_into_es, add_staged_pdf


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
            'content': []
        }
        input = request.data
        if input != {}:
            query = input["query"]
            res = search.search(query, 10)
            response['success'] = True
            response['totalResult'] = res['hits']
            content = res['results']
            for c in content:
                response['content'].append(c.frontend_result())
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


# files, adds file to db and filesystem.
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
