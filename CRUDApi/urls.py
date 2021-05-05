from django.urls import path
from . import views

urlpatterns = [
    path('getStudent',views.student_api),
    path('getStudentModel',views.ModelBased.as_view()),
]