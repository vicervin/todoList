from rest_framework import serializers
from .models import ToDoList
from django.contrib.auth.models import User


class ToDoListSerializer(serializers.ModelSerializer):
    """ Serializer to map model instance to JSON format """

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        """ Meta class for mapping serialiters fields with model fields"""

        model = ToDoList
        fields = ('id', 'name', 'owner', 'date_created', 'date_altered', 'done')
        read_only_fields = ('date_created', 'date_altered')


class UserSerializer(serializers.ModelSerializer):
    """A user serializer to aid in authentication and authorization."""

    todolists = serializers.PrimaryKeyRelatedField(
        many=True, queryset=ToDoList.objects.all())

    class Meta:
        """Map this serializer to the default django user model."""
        model = User
        fields = ('id', 'username', 'todolists')