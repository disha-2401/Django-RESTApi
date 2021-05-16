from django.shortcuts import render
from .serializer import StudentSerializer
from rest_framework import viewsets
from .models import Student
# Create your views here.


class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer