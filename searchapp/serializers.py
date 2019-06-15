from searchapp.models import CarModel
from rest_framework import serializers


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ('__all__')
