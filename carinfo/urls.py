from django.urls import path
from . import views

urlpatterns = [
    path('', views.CarInformationView.as_view()),
]
