from django.urls import path
from . import views

urlpatterns = [
    path('hello',views.hello),
    path('StudentInfo/',views.StudentsInfo),
    path('StudentInfo/<int:pk>',views.StudentsInfo)
]