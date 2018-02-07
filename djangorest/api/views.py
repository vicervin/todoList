from django.shortcuts import render
from rest_framework import generics, permissions
from .serializers import ToDoListSerializer, UserSerializer
from django.contrib.auth.models import User
from .models import ToDoList
from .permissions import IsOwner
from .decorators import logger


class CreateView(generics.ListCreateAPIView):
    """ This class defines the view"""
    queryset = ToDoList.objects.all()
    serializer_class = ToDoListSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner)

    @logger
    def perform_create(self, serializer):
        """ Save the post data when creating a todolist"""
        serializer.save(owner=self.request.user)


class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """ This class handles the view which reads, updates and deletes requests """

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