from faker import Faker
from faker.providers import automotive, barcode, company, currency, lorem
from searchapp.serializers import CarSerializer


class FakerCarData:
    fake = Faker()

    def fake_headline(self):
        return self.fake.name()

    def fake_manufacturer(self):
        return self.fake.company()

    def fake_car_model(self):
        return self.fake.company_suffix()

    def fake_car_type(self):
        return self.fake.cryptocurrency_name()

    def fake_engine_type(self):
        return self.fake.license_plate()

    def fake_chasis_number(self):
        return self.fake.ean(length=13)

    def fake_description(self):
        return self.fake.sentence(nb_words=6, variable_nb_words=True, ext_word_list=None)

    def fake_tags(self, **kwargs):
        return str(kwargs['headline']) + ', ' + str(kwargs['manufacturer']) + ', ' + str(kwargs['car_model'] + ', ' +
                    str(kwargs['car_type'] + ', ' + str(kwargs['engine_type'])))

    def fake_price(self):
        return self.fake.ean(length=8)


"""fake = Faker()


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
    print('created_at -> ' + '2019-06-18 12:00:05' + ' ')"""
