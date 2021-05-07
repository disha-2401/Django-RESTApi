from django.urls import path
from . import views

urlpatterns = [
    path('StudentAPI/',views.StudentApi.as_view()),
    path('StudentAPI/<int:pk>',views.StudentApi.as_view()),
]