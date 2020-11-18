from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CarInfoSerializer
from .models import CarInformation, PictureCar
from rest_framework import generics
from django.http import Http404
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated


class CarInformationView(generics.ListCreateAPIView):
    queryset = CarInformation.objects.all()
    serializer_class = CarInfoSerializer
    permission_classes = [IsAuthenticated]
    
    #method가 get일때 모든 차량정보와 사진을 리턴
    def get(self, APIView):
        carinfo = CarInformation.objects.all().values()
        picture = PictureCar.objects.all().values()
        data={"carinformation":carinfo, "pictures":picture}

        return Response(data)

class CarInformationDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return CarInformation.objects.get(pk=pk)
        except CarInformation.DoesNotExist:
            return Http404

    def get(self, request, pk):
        carinfo = self.get_object(pk)
        carserializer = CarInfoSerializer(carinfo)
        picture = PictureCar.objects.filter(car_information_id=pk).values()
        data={"carinformation":carserializer.data, "pictures":picture}
        
        return Response(data)
    
    def put(self, request, pk):
        carinfo = self.get_object(pk)
        serializer = CarInfoSerializer(carinfo, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, reuqest, pk):
        carinfo = self.get_object(pk)
        carinfo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
