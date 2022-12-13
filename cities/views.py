from django.shortcuts import render
from rest_framework import mixins, viewsets

from .models import Country,City,County,RuralDistrict,Province
from .serializers import CountySerializer,CountrySerializer,RuralDistrictSerializer,CitySerializer,ProvinceSerializer
# Create your views here.



class CountryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    lookup_field = 'pk'  # default

class ProvinceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Province.objects.all()
    serializer_class = ProvinceSerializer
    lookup_field = 'pk'  # default

class CountyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = County.objects.all()
    serializer_class = CountySerializer
    lookup_field = 'pk'  # default

class CityViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    lookup_field = 'pk'  # default

class RuralDistrictViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = RuralDistrict.objects.all()
    serializer_class = RuralDistrictSerializer
    lookup_field = 'pk'  # default
