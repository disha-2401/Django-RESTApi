import io

from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from .serializer import StudentSerializer
from .models import Student
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse

@api_view(['GET','POST'])
def hello(request):
    if request.method == "GET":
        return Response({'msg':'this is get request'})
    elif request.method == "POST":
        return Response(request.data)


@api_view(['GET','POST'])
def StudentsInfo(request):
    if request.method == "GET":
        id = request.data.get('id')
        if id is not None:
            student=Student.objects.get(id=id)
            serializer=StudentSerializer(student)
            return Response(serializer.data)
        student = Student.objects.all()
        serializer = StudentSerializer(student,many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'object created'})
        else:
            return Response(serializer.errors)
