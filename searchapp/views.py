from django.shortcuts import render
from django.views.generic import View
from django.views.generic.base import TemplateView
from rest_framework import generics
from searchapp.configs import *
from searchapp.serializers import CarSerializer
from searchapp.models import CarModel, CarModelManager
from searchapp.forms import CarCreationFrom

# Create your views here.
class AllCarsAPIView(generics.ListAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer


class CreateCarAPIView(generics.CreateAPIView):
    serializer_class = CarSerializer

    def post(self, **kwargs):
        return True


class CreateFakeCarData(View):
    model = CarModel
    serializer_class = CarSerializer
    form_class = CarCreationFrom
    template_name = 'car-add-view.html'
    initial = {'key': 'value'}
    api_view = CreateCarAPIView()
    request_method = 'get'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form, 'request_method': self.request_method})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            total_numbers = form.cleaned_data['total_numbers']
            form = self.form_class(initial=self.initial)

            if self.api_view.post(total_numbers = total_numbers):
                self.request_method = 'successpost'
            else:
                self.request_method = 'errorpost'

            return render(request, self.template_name, {'form': form, 'request_method': self.request_method})
        else:
            self.request_method = 'errorpost'
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form': form, 'request_method': self.request_method})
