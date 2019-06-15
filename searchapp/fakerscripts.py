from faker import Faker
from faker.providers import automotive, barcode, company, currency, lorem
#from searchapp.configs import *
#from searchapp.models import CarModel, CarModelManager
#from searchapp.serializers import CarSerializer


fake = Faker()


for _ in range(10):

    print('headline -> ' + str(fake.name()) + ' ')
    print('manufacturer -> ' + str(fake.company()) + ' ')
    print('car model -> ' + str(fake.company_suffix()) + ' ')
    print('car type -> ' + str(fake.cryptocurrency_name()) + ' ')
    print('chasis number -> ' + str(fake.ean(length=13)) + ' ')
    print('description -> ' + str(fake.sentence(nb_words=6, variable_nb_words=True, ext_word_list=None)) + ' ')
    print('tags -> ' + str(fake.company()) + ', ' + str(fake.company_suffix()) + ', ')
    print('price -> ' + str(fake.ean(length=8)) + ' ')
    print('is active -> ' + '1' + ' ')
    print('created_at -> ' + '2019-06-18 12:00:05' + ' ')
