import json
from django.core.management.base import BaseCommand
from cities.models import Country, City, County, Province, RuralDistrict


class Command(BaseCommand):

    def handle(self, *args, **options):
        with open('cities/fixtures/countries.json') as f:
            data_list = json.load(f)

        for data in data_list:
            data.pop('created_at')
            data.pop('updated_at')
            data['pk'] = data.pop('id')
            Country.objects.get_or_create(pk=data['pk'], defaults=data)

        with open('cities/fixtures/provinces.json') as f:
            data_list = json.load(f)

        for data in data_list:
            data.pop('created_at')
            data.pop('updated_at')
            data['pk'] = data.pop('id')
            Province.objects.get_or_create(pk=data['pk'], defaults=data)

        with open('cities/fixtures/counties.json') as f:
            data_list = json.load(f)

        for data in data_list:
            data.pop('created_at')
            data.pop('updated_at')
            data['pk'] = data.pop('id')
            County.objects.get_or_create(pk=data['pk'], defaults=data)

        with open('cities/fixtures/cities.json') as f:
            data_list = json.load(f)

        for data in data_list:
            data.pop('created_at')
            data.pop('updated_at')
            data['pk'] = data.pop('id')
            City.objects.get_or_create(pk=data['pk'], defaults=data)

        with open('cities/fixtures/rural_districts.json') as f:
            data_list = json.load(f)

        for data in data_list:
            data.pop('created_at')
            data.pop('updated_at')
            data['pk'] = data.pop('id')
            RuralDistrict.objects.get_or_create(pk=data['pk'], defaults=data)



