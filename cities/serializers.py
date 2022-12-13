from rest_framework import serializers

from .models import Country,City,County,RuralDistrict,Province

class CountrySerializer(serializers.ModelSerializer):

    class Meta:
        model = Country
        fields = [
            'pk',
            'name',
            'url'
        ]


class ProvinceSerializer(serializers.ModelSerializer):
    country = CountrySerializer()
    class Meta:
        model = Province
        fields = [
            'pk',
            'country',
            'name',
            'url'
        ]

class CitySerializer(serializers.HyperlinkedModelSerializer):
    province = ProvinceSerializer()
    class Meta:
        model = City
        fields = [
            'pk',
            'province',
            'name',
            'url'
        ]
class CountySerializer(serializers.HyperlinkedModelSerializer):
    province = ProvinceSerializer()

    class Meta:
        model = County
        fields = [
            'pk',
            'province',
            'name',
            'url'
        ]

class RuralDistrictSerializer(serializers.HyperlinkedModelSerializer):
    province = ProvinceSerializer()

    class Meta:
        model = RuralDistrict
        fields = [
            'pk',
            'province',
            'county',
            'name',
            'url'
        ]