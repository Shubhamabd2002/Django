from django.shortcuts import render
from rest_framework import generics
from . import serializers
from . import models
# Create your views here.
class TodoGetViews(generics.ListAPIView):
    queryset = models.Todo.objects.all()
    serializer_class = serializers.TodoSerializers

class TodoCreateViews(generics.CreateAPIView):
    queryset = models.Todo.objects.all()
    serializer_class = serializers.TodoSerializers

# class TodoCreateViews(generics.UpdateAPIView):
#     queryset = models.Todo.objects.all()
#     serializer_class = serializers.TodoSerializers

