from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

# create router object
router = DefaultRouter()

# register studentViewSet class
router.register('studentApi', views.StudentViewSet, basename='student')
urlpatterns = [
    path('viewSet/', include(router.urls))
]
