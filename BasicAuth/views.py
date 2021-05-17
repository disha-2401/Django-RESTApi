from django.shortcuts import render
from .serializer import StudentSerializer
from rest_framework import viewsets
from .models import Student
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser
# Create your views here.


class StudentModelAuth(viewsets.ModelViewSet):  # ReadOnlyModelViewSet to make tit readonly
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAdminUser]