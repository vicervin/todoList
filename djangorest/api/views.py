from django.shortcuts import render
from rest_framework import generics, permissions
from .serializers import ToDoListSerializer, UserSerializer
from django.contrib.auth.models import User
from .models import ToDoList
from .permissions import IsOwner


class CreateView(generics.ListCreateAPIView):
    """ This class defines the create behaviour of the API"""
    queryset = ToDoList.objects.all()
    serializer_class = ToDoListSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner)

    def perform_create(self, serializer):
        """ Save the post data when creating a todolist"""
        serializer.save(owner=self.request.user)


class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """ This class handles reading, updating and deleting requests """

    queryset = ToDoList.objects.all()
    serializer_class = ToDoListSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner)


class UserView(generics.ListAPIView):
    """View to list the user queryset."""
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailsView(generics.RetrieveAPIView):
    """View to retrieve a user instance."""
    queryset = User.objects.all()
    serializer_class = UserSerializer