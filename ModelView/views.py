from django.shortcuts import render
from .serializer import StudentSerializer
from rest_framework import viewsets
from .models import Student
# Create your views here.


class StudentModelViewSet(viewsets.ModelViewSet): #ReadOnlyModelViewSet to make tit readonly
    queryset = Student.objects.all()
    serializer_class = StudentSerializer