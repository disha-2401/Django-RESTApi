from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

# create router object
router = DefaultRouter()

# register studentViewSet class
# router.register('student', views.StudentModelViewSet, basename='student')
urlpatterns = [
    path('ModelViewSet/', include(router.urls)),
]
