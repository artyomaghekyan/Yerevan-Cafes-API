from django.shortcuts import render
from .serializers import CafeSerializer
from rest_framework.views import APIView
from .models import Cafes
from rest_framework.response import Response
from django.db.models import Q 
from rest_framework import status, generics
from rest_framework.permissions import IsAdminUser
from django.urls import reverse_lazy


# Create your views here.


class Endpoints(APIView):

    def get(self, request):
        data = ['cafes/', 'name/cafe-name', 'rating/cafe-rating']
        return Response(data)


class CafeList(generics.ListCreateAPIView):
    queryset = Cafes.objects.all()
    serializer_class = CafeSerializer
    success_url = reverse_lazy('all')


    def list(self, request):
        queryset = self.get_queryset()
        serializer = CafeSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class CafeDetail(APIView):
    
    def get(self, request, name):
        cafe = Cafes.objects.get(name=name)
        serializer = CafeSerializer(cafe, many=False)
        return Response(serializer.data)


class CafeRating(APIView):
    def get(self, request, rating):
        cafe = Cafes.objects.filter(rating=rating)
        serializer = CafeSerializer(cafe, many=True)
        return Response(serializer.data)