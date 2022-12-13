import json
from django.core.management.base import BaseCommand

from createForm.models import Attribute


class Command(BaseCommand):

    def handle(self, *args, **options):
        with open('createForm/fixtures/attributes.json') as f:
            data_list = json.load(f)

        for data in data_list:
            data['pk'] = data.pop('id')
            Attribute.objects.get_or_create(pk=data['pk'], defaults=data)
