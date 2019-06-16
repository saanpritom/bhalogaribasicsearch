from django.urls import path
from apps.apiconsumer import views

urlpatterns = [
    path('create/', views.CreateFakeCarData.as_view(), name='create-cars'),
]
