from django.urls import path
from . import views
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('register/', views.Register.as_view()),
    path('login/', obtain_jwt_token)
]
