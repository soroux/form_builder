from rest_framework import serializers

from api.serializers import UserPublicSerializer
from .models import DataType, Attribute, DataAttribute, LimitEntry


class DataTypePublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataType
        fields = ['pk', 'name']


class LimitEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = LimitEntry
        fields = ['pk', 'name']


class DataAttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataAttribute
        fields = ['pk', 'name', 'max', 'min', 'min_length', 'max_length', 'default', 'use_in_children', 'order',
                  'attribute', 'dataType']

    def validate(self, data):
        print(data['use_in_children'], data['dataType'].is_first_parent)
        if data['use_in_children'] == True and data['dataType'].is_first_parent is False:
            raise serializers.ValidationError("use in children only available on first parent dataTypes")
        return data


class DataTypeSerializer(serializers.ModelSerializer):
    user = UserPublicSerializer(read_only=True)
    dataAttributes = DataAttributeSerializer(read_only=True, many=True)

    class Meta:
        model = DataType
        fields = ['pk', 'url', 'name', 'slug', 'parent', 'user', 'created_at', 'dataAttributes', 'is_first_parent',
                  'limit_entry']


class AttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attribute
        fields = ['pk', 'url', 'name', 'min', 'max', 'fa_name', 'default', 'min_length', 'max_length']
