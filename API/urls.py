from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('test', views.testView.as_view()),
    path('BTS/<int:pk>', views.MemberDetails),
    path('BTS', views.AllMemberDetails),
    path('BTSCreate/', views.MemberCreate),
]
