from django.shortcuts import render
from django.views.generic import View
from django.views.generic.base import TemplateView
from rest_framework import generics, status
from rest_framework.response import Response
from searchapp.configs import *
from searchapp.serializers import CarSerializer
from searchapp.models import CarModel, CarModelManager
from searchapp.forms import CarCreationFrom
from searchapp.fakerscripts import FakerCarData

# Create your views here.
class AllCarsAPIView(generics.ListAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer


class CreateCarAPIView(generics.CreateAPIView):
    serializer_class = CarSerializer


class CreateFakeCarData(View):
    model = CarModel
    serializer_class = CarSerializer
    form_class = CarCreationFrom
    faker_script_class = FakerCarData()
    template_name = 'car-add-view.html'
    initial = {'key': 'value'}
    api_endpoint = str(base_url) + '/api/v1/cars/create/'
    request_method = 'get'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form, 'request_method': self.request_method})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            total_numbers = form.cleaned_data['total_numbers']
            form = self.form_class(initial=self.initial)

            counter_flag = 1

            for _ in range(int(total_numbers)):

                #calling faker agent to create fake dataset
                headline = self.faker_script_class.fake_headline()
                manufacturer = self.faker_script_class.fake_manufacturer()
                car_model = self.faker_script_class.fake_car_model()
                car_type = self.faker_script_class.fake_car_type()
                engine_type = self.faker_script_class.fake_engine_type()
                chasis_number = self.faker_script_class.fake_chasis_number()
                description = self.faker_script_class.fake_description()
                tags = self.faker_script_class.fake_tags(headline = headline,
                                                         manufacturer = manufacturer,
                                                         car_model = car_model,
                                                         car_type = car_type,
                                                         engine_type = engine_type)
                price = self.faker_script_class.fake_price()
                is_active = config_is_active

                #hitting the CreateAPI Endpoint
                hit_api = 'self.api_endpoint headline="headline"'

                if hit_api.status == status.HTTP_201_CREATED:
                    counter_flag = counter_flag + 1
                    continue
                else:
                    break

            if counter_flag == int(total_numbers):
                self.request_method = 'successpost'
            else:
                self.request_method = 'errorpost'

            return render(request, self.template_name, {'form': form, 'request_method': self.request_method})
        else:
            self.request_method = 'errorpost'
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form': form, 'request_method': self.request_method})
