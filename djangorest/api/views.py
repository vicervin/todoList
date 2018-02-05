from django.shortcuts import render
from rest_framework import generics
from .serializers import ToDoListSerializer
from .models import ToDoList

class CreateView(generics.ListCreateAPIView):
    """ This class defines the create behaviour of the API"""
    queryset = ToDoList.objects.all()
    serializer_class = ToDoListSerializer

    def perform_create(self, serializer):
        """ Save the post data when creating a todolist"""
        serializer.save()

class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """ This class handles reading, updating and deleting requests """

    queryset = ToDoList.objects.all()
    serializer_class = ToDoListSerializer
