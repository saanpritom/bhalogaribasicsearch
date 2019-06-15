from django.urls import path
from searchapp import views

urlpatterns = [
    path('v1/cars/', views.AllCarsAPIView.as_view(), name='all-cars'),
    path('v1/cars/create/', views.CreateCarAPIView.as_view(), name='create-cars'),
]
