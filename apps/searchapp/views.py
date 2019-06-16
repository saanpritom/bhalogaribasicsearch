from django.shortcuts import render, Http404
from django.views.generic import View
from django.views.generic.base import TemplateView
from rest_framework import generics, status
from rest_framework.response import Response
from apps.searchapp.configs import *
from apps.searchapp.serializers import CarSerializer
from apps.searchapp.models import CarModel, CarModelManager
from apps.searchapp.forms import CarCreationFrom
from apps.searchapp.fakerscripts import FakerCarData

# Create your views here.
class AllCarsAPIView(generics.ListAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer


class CreateCarAPIView(generics.CreateAPIView):
    serializer_class = CarSerializer


class CarDetailAPIView(generics.RetrieveAPIView):
    serializer_class = CarSerializer
    model = CarModel

    def get_object(self, pk):
        try:
            return self.model.objects.get(pk=pk)
        except self.model.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        car = self.get_object(pk)
        serializer = self.serializer_class(car)
        return Response(serializer.data)
