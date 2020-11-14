from rest_framework import serializers
from .models import CarInformation


class CarInfoSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = CarInformation
        fields = ('__all__')
