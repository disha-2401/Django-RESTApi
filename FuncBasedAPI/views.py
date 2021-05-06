import io

from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from .serializer import StudentSerializer
from .models import Student
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse


@api_view(['GET', 'POST'])
def hello(request):
    if request.method == "GET":
        return Response({'msg': 'this is get request'})
    elif request.method == "POST":
        return Response(request.data)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def StudentsInfo(request):
    if request.method == "GET":
        id = request.data.get('id')
        if id is not None:
            student = Student.objects.get(id=id)
            serializer = StudentSerializer(student)
            return Response(serializer.data)
        student = Student.objects.all()
        serializer = StudentSerializer(student, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'object created'})
        else:
            return Response(serializer.errors)
    elif request.method == "PUT":
        id = request.data.get('id')
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'object updated'})
        return Response(serializer.errors)
    elif request.method == 'DELETE':
        id = request.data.get('id')
        try:
            stu = Student.objects.get(id=id)
        except ObjectDoesNotExist:
            return Response({'msg': 'object does not exist'})
        stu.delete()
        return Response({'msg': 'object deleted'})
