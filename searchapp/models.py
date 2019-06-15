from django.db import models
from django.utils import timezone
from django.db.models import Q

# Create your models here.
class CarModelManager(models.Manager):

    def check_chasis_number(self, chasis_number):
        return chasis_number


class CarModel(models.Model):
    headline = models.CharField(max_length=60, null=False, unique=False)
    manufacturer = models.CharField(max_length=60, null=False, unique=False)
    car_model = models.CharField(max_length=60, null=False, unique=False)
    car_type = models.CharField(max_length=60, null=False, unique=False)
    engine_type = models.CharField(max_length=60, null=False, unique=False)
    chasis_number = models.CharField(max_length=60, null=False, unique=True)
    description = models.CharField(max_length=120, null=False, unique=False)
    tags = models.CharField(max_length=60, null=False, unique=False)
    price = models.CharField(max_length=60, null=False, unique=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    REQUIRED_FIELDS = ['headline', 'manufacturer', 'car_model', 'car_type', 'engine_type', 'chasis_number', 'price']

    objects = CarModelManager()

    def __str__(self):
        return self.headline
