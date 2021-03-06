from django.urls import path
from apps.apiconsumer import views

urlpatterns = [
    path('', views.AllCarsView.as_view(), name='all-cars-view'),
    path('create/', views.CreateFakeCarData.as_view(), name='create-cars'),
    path('detail/<int:pk>/', views.DetailCarView.as_view(), name='detail-car'),
    path('search/', views.SearchCarView.as_view(), name='search-car'),
]
