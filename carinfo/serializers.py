from rest_framework import serializers
from .models import CarInformation, PictureCar

class PictureCarSerializer(serializers.HyperlinkedModelSerializer):
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = PictureCar
        fields = ('image')

class CarInfoSerializer(serializers.ModelSerializer):
    images = PictureCarSerializer(many=True, read_only=True)
    
    class Meta:
        model = CarInformation
        fields = ('id', 'user', 'accident_history', 'repair_report', 'manufacturer', 'foreign_car', 'desired_price', 'created_at', 'images')

    def create(self, validated_data):
        images_data = self.context['request'].FILES
        carinfo = CarInformation.objects.create(**validated_data)
        for image_data in images_data.getlist('image'):
            picture = PictureCar.objects.create(car_information_id=carinfo, image=image_data)
        
        return carinfo
