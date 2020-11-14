from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CarInfoSerializer
from .models import CarInformation
from rest_framework import generics

# Create your views here.   
class CarInformationView(generics.ListCreateAPIView):
    queryset = CarInformation.objects.all()
    serializer_class = CarInfoSerializer
    
