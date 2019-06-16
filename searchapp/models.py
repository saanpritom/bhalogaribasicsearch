from django.db import models
from django.utils import timezone
from django.db.models import Q

# Create your models here.
class CarModelManager(models.Manager):

    def check_chasis_number(self, chasis_number):
        existed_car_id = self.model.objects.filter(chasis_number = chasis_number).count()

        if existed_car_id > 0:
            return True
        else:
            return False

    def create_fake_data(self, **model_data):
        car_object = self.model.objects.create(headline = model_data['headline'],
                                               manufacturer = model_data['manufacturer'],
                                               car_model = model_data['car_model'],
                                               car_type = model_data['car_type'],
                                               engine_type = model_data['engine_type'],
                                               chasis_number = model_data['chasis_number'],
                                               description = model_data['description'],
                                               tags = model_data['tags'],
                                               price = model_data['price'])

        car_object.save()
        return car_object.id


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
