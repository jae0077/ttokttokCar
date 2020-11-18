from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CreateUserSerializer, LoginSerializer
from django.http import HttpResponse
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated

#회원가입 view
class Register(APIView):
    permission_classes = (AllowAny,)
    def post(self, request, format=None):
        serializer = CreateUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            message = {"message" : serializer.data['nickname'] +  "님 환영합니다."}
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#로그인view
class Login(APIView):
    permission_classes = (AllowAny,)
    def post(self, request, format=None):
        serializer = LoginSerializer(data=request.data)
        
        if serializer.is_valid():
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

