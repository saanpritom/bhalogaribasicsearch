from django.urls import path
from searchapp import views

urlpatterns = [
    path('v1/cars/', views.AllCars.as_view(), name='all-cars'),
]
