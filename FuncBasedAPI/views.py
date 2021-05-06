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
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse


@api_view(['GET', 'POST'])
def hello(request):
    if request.method == "GET":
        return Response({'msg': 'this is get request'})
    elif request.method == "POST":
        return Response(request.data)


@api_view(['GET', 'POST', 'PUT', 'DELETE','PATCH'])
def StudentsInfo(request,pk=None):
    if request.method == "GET":
        id = pk
        if id is not None:
            student = Student.objects.get(id=id)
            serializer = StudentSerializer(student)
            return Response(serializer.data,status=status.HTTP_200_OK)
        student = Student.objects.all()
        serializer = StudentSerializer(student, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method == "POST":
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'object created'},status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "PUT":
        id = pk
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'complete object updated'},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "PATCH":
        id = pk
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'partial object updated'},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        id = pk
        try:
            stu = Student.objects.get(id=id)
        except ObjectDoesNotExist:
            return Response({'msg': 'object does not exist'},status=status.HTTP_404_NOT_FOUND)
        stu.delete()
        return Response({'msg': 'object deleted'},status=status.HTTP_200_OK)
