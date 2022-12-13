# from django.shortcuts import render
# from rest_framework import generics
#
# # Create your views here.
# from tags.models import Tag
# from tags.serializers import TagSerializer
#
#
# class TagsListView(generics.ListAPIView):
#     queryset = Tag.objects.all()
#     serializer_class = TagSerializer
#
# class TagDetailView(generics.RetrieveAPIView):
#     queryset = Tag.objects.all()
#     serializer_class = TagSerializer
#
#
# class TagCreateView(generics.CreateAPIView):
#     queryset = Tag.objects.all()
#     serializer_class = TagSerializer
#
#
# class TagUpdateView(generics.UpdateAPIView):
#     queryset = Tag.objects.all()
#     serializer_class = TagSerializer
#     lookup_field = 'pk'
#
# class TagDestroyView(generics.DestroyAPIView):
#     queryset = Tag.objects.all()
#     serializer_class = TagSerializer
#     lookup_field = 'pk'
