import io

from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import BookSerializer,BTSMembersSerializer
from .models import Book,BTSMembers
from rest_framework.renderers import JSONRenderer
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls={
        'List': '/task-list',
        'Detail-view':'/task-detail/<str:pk>',
        'Create':'/task-create/',
        'Update':'/task-update/<str:pk>',
        'Delete':'/task-delete/<str:pk>',
    }
    return Response(api_urls)

class testView(APIView):
    def get(self,request,*args,**kwargs):
        qs=Book.objects.all()
        serializer=BookSerializer(qs,many=True)
        return Response(serializer.data)

    def post(self,request,*args,**kwargs):
        serializer=BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


def MemberDetails(request,pk):
    member=BTSMembers.objects.get(id=pk)
    BtsSerializer=BTSMembersSerializer(member)
    # Json_data=JSONRenderer().render(BtsSerializer.data)
    # return HttpResponse(Json_data,content_type='application/json')
    return JsonResponse(BtsSerializer.data,safe=True)

def AllMemberDetails(request):
    member=BTSMembers.objects.all()
    BtsSerializer=BTSMembersSerializer(member,many=True)
    # Json_data=JSONRenderer().render(BtsSerializer.data)
    # return HttpResponse(Json_data,content_type='application/json')
    return JsonResponse(BtsSerializer.data,safe=False)

@csrf_exempt
def MemberCreate(request):
    if request.method == 'POST':
        print("POST")
        json_data=request.body
        stream = io.BytesIO(json_data)
        print(stream)
        jsonData=JSONParser().parse(stream)
        print(jsonData.get('id',None))
        serializer=BTSMembersSerializer(data=jsonData)
        if serializer.is_valid():
            serializer.save()
            print("valid")
            res={'message':'row created'}
            json_data=JSONRenderer().render(res) 
            return JsonResponse(serializer.data,safe=False)
        return JsonResponse(serializer.errors, safe=False)
    return HttpResponse("error")