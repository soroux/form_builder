from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, viewsets, permissions
from rest_framework import filters

from api.permissions import IsOwner
from .models import Tag
from .serializers import TagSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    lookup_field = 'pk'  # default
    permission_classes = [IsOwner]
    filterset_fields = ['name']
    filter_backends = [filters.SearchFilter,DjangoFilterBackend,filters.OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['name', 'pk']

    def get_queryset(self, *args, **kwargs):
        return Tag.objects.all().filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)