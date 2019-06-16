from django.shortcuts import render, Http404
from django.views.generic import View
from django.views.generic.base import TemplateView
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework.response import Response
from apps.searchapp.configs import *
from apps.searchapp.serializers import CarSerializer
from apps.searchapp.models import CarModel, CarModelManager
from apps.searchapp.dictionary import *

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


class CarSearchAPIView(APIView):
    model = CarModel
    serializer_class = CarSerializer

    def get_all_object(self):
        try:
            return self.model.objects.filter(is_active = True)
        except self.model.DoesNotExist:
            raise Http404

    def get_searched_object(self, querystring):
        try:
            return self.model.objects.filter(Q(tags__icontains = querystring) | Q(description__icontains = querystring) |
                                                Q(price__icontains = querystring) | Q(chasis_number__icontains = querystring), is_active = True,)
        except self.model.DoesNotExist:
            raise Http404

    def get(self, request, format=None, **kwargs):
        keyword = kwargs['search']

        #making all entry lowered case
        keyword = keyword.lower()

        #check if the keyword is in the car dictionary list
        if keyword in car_words:
            cars = self.get_all_object()
        else:
            cars = self.get_searched_object(keyword)

        serializer = self.serializer_class(cars, many=True)
        return Response(serializer.data)
