from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

# create router object
router = DefaultRouter()

# register studentViewSet class
router.register('studentApi', views.StudentModelAuth, basename='student')
urlpatterns = [
    path('Auth/', include(router.urls)),
]