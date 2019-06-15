from django.shortcuts import render
from django.views.generic.base import TemplateView
from rest_framework import generics
from searchapp.configs import *
from searchapp.serializers import CarSerializer
from searchapp.models import CarModel

# Create your views here.
class AllCarsAPIView(generics.ListAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer


class CreateCarAPIView(generics.CreateAPIView):
    serializer_class = CarSerializer
