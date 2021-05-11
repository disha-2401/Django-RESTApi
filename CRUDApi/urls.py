from django.urls import path
from . import views

urlpatterns = [
    path('StudentInfo',views.student_api),
    path('StudentInfoModel',views.ModelBased.as_view()),
]