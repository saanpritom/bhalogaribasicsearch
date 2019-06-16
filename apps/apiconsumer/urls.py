from django.urls import path
from apps.apiconsumer import views

urlpatterns = [
    path('', views.AllCarsView.as_view(), name='all-cars'),
    path('create/', views.CreateFakeCarData.as_view(), name='create-cars'),
]
