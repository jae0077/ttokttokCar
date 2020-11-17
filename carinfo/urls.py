from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.CarInformationView.as_view()),
    path('<int:pk>', views.CarInformationDetailView.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)
