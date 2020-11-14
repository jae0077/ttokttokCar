from rest_framework import serializers
from .models import ttokttokCarUser

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

