from rest_framework import serializers
from .models import ttokttokCarUser
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login

class CreateUserSerializer(serializers.Serializer):
    nickname = serializers.CharField(max_length=20)
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(max_length=30)
    
    def create(self, validated_data):
        user = ttokttokCarUser.objects.create(
                nickname = validated_data['nickname'],
                email = validated_data['email'],
        )
        user.set_password(validated_data['password'])
        
        user.save()
        return user

class LoginSerializer(serializers.Serializer):
    nickname = serializers.CharField(max_length=20)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)


    def validate(self, data):
        nickname = data.get('nickname', None)
        password = data.get('password', None)
        print (nickname, password)
        user = authenticate(nickname=nickname, password=password)
        if user is None:
           raise serializers.ValidationError(
                   'login fail'
                   )
        try:
            token, flag = Token.objects.get_or_create(user=user)
            print (flag)
            update_last_login(None, user)
        except ttokttokCarUser.DoesNotExist:
            raise serializers.ValidationError(
                    'User with given email and password does not exists'
                    )
        return {
                'nickname':user.nickname,
                'token': token.key
                }
