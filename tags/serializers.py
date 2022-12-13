from rest_framework import serializers
from api.serializers import UserPublicSerializer

from .models import Tag

class TagSerializer(serializers.ModelSerializer):
    user = UserPublicSerializer(read_only=True)

    class Meta:
        model = Tag
        fields = [
            'pk',
            'user',
            'name',
            'slug',
            'url'
        ]