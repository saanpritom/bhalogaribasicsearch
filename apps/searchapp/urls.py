from django.urls import path
from apps.searchapp import views

urlpatterns = [
    path('v1/cars/', views.AllCarsAPIView.as_view(), name='all-cars-api-view'),
    path('v1/cars/create/', views.CreateCarAPIView.as_view(), name='create-cars-api-view'),
    path('v1/car/<int:pk>/', views.CarDetailAPIView.as_view(), name='car-detail-api-view'),
    path('v1/cars/search/<str:search>/', views.CarSearchAPIView.as_view(), name='car-search-api-view'),
]
