from django.shortcuts import render, Http404
from django.views.generic import View
from apps.searchapp.configs import *
from apps.searchapp.models import CarModel
from apps.apiconsumer.fakerscripts import FakerCarData
from apps.apiconsumer.forms import CarCreationFrom, CarSearchForm
from apps.apiconsumer.apis import *
import json, requests

# Create your views here.
class CreateFakeCarData(View):
    model = CarModel
    form_class = CarCreationFrom
    faker_script_class = FakerCarData()
    template_name = 'car-add-view.html'
    initial = {'key': 'value'}
    request_method = 'get'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form, 'request_method': self.request_method})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            total_numbers = form.cleaned_data['total_numbers']
            form = self.form_class(initial=self.initial)

            counter_flag = 0

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
                is_active = True

                #check if the chasis number is already exists or not
                if self.model.objects.check_chasis_number(chasis_number):
                    chasis_number = chasis_number
                else:
                    chasis_number = str(chasis_number) + str(price)

                #call the save function and save the data
                new_car_data = self.model.objects.create_fake_data(headline = headline,
                                                                    manufacturer = manufacturer,
                                                                    car_model = car_model,
                                                                    car_type = car_type,
                                                                    engine_type = engine_type,
                                                                    chasis_number = chasis_number,
                                                                    description = description,
                                                                    tags = tags,
                                                                    price = price)

                if int(new_car_data):
                    counter_flag = counter_flag + 1
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


class AllCarsView(View):
    api_endpoint = api_endpoints['all_cars']
    template_name = 'all_cars_view.html'

    def request_api(self):
        response = requests.get(self.api_endpoint)
        return response

    def get(self, request, *args, **kwargs):
        api_response = self.request_api()
        jsonify_data = json.loads(api_response.content)
        return render(request, self.template_name, {'api_response': api_response, 'datas': jsonify_data})


class DetailCarView(View):
    api_endpoint = api_endpoints['single_car']
    template_name = 'car_detail_view.html'

    def request_api(self, car_id):
        car_id_api_endpoint = str(self.api_endpoint) + str(car_id) + '/'
        response = requests.get(car_id_api_endpoint)
        return response

    def get(self, request, *args, **kwargs):
        car_id = kwargs['pk']
        api_response = self.request_api(car_id)
        jsonify_data = json.loads(api_response.content)
        return render(request, self.template_name, {'api_response': api_response, 'datas': jsonify_data})


class SearchCarView(View):
    api_endpoint = api_endpoints['car_search']
    template_name = 'search-view.html'

    def request_api(self, search_keyword):
        search_keyword_api_endpoint = str(self.api_endpoint) + str(search_keyword) + '/'
        response = requests.get(search_keyword_api_endpoint)
        return response

    def get(self, request, *args, **kwargs):
        search_keyword = 'all'
        api_response = self.request_api(search_keyword)
        jsonify_data = json.loads(api_response.content)
        return render(request, self.template_name, {'api_response': api_response, 'datas': jsonify_data, 'search_keyword': search_keyword})
