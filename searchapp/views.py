from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.
class AllCars(TemplateView):
    template_name = 'all-cars-view.html'
