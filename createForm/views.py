from django.shortcuts import render

# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from rest_framework.permissions import DjangoModelPermissions

from api.permissions import IsOwner
from createForm.models import Attribute, DataType, DataAttribute, LimitEntry
from createForm.serializers import AttributeSerializer, DataTypeSerializer, DataAttributeSerializer, \
    LimitEntrySerializer


class AttributeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Attribute.objects.all()
    serializer_class = AttributeSerializer
    lookup_field = 'pk'  # default

class LimitEntryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = LimitEntry.objects.all()
    serializer_class = LimitEntrySerializer
    lookup_field = 'pk'  # default

class DataTypeViewSet(viewsets.ModelViewSet):
    queryset = DataType.objects.all()
    serializer_class = DataTypeSerializer
    lookup_field = 'pk'  # default
    permission_classes = [DjangoModelPermissions,IsOwner]
    filterset_fields = ['name','parent']
    filter_backends = [filters.SearchFilter,DjangoFilterBackend,filters.OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['name', 'created_at']

    def get_queryset(self, *args, **kwargs):
        return DataType.objects.all().filter(user=self.request.user)
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class DataAttributeViewSet(viewsets.ModelViewSet):
    queryset = DataAttribute.objects.all()
    serializer_class = DataAttributeSerializer
    lookup_field = 'pk'  # default
    permission_classes = [DjangoModelPermissions, IsOwner]
    filterset_fields = ['name','dataType__id']
    filter_backends = [filters.SearchFilter, DjangoFilterBackend, filters.OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['name', 'created_at']

    def get_queryset(self, *args, **kwargs):
        return DataAttribute.objects.all().filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)