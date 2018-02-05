from rest_framework import serializers
from .models import ToDoList

class ToDoListSerializer(serializers.ModelSerializer):
    """ Serializer to map model instance to JSON format """

    class Meta:
        """ Meta class for mapping serialiters fields with model fields"""

        model = ToDoList
        fields = ('id', 'name', 'date_created', 'date_altered', 'done')
        read_only_fields = ('date_created', 'date_altered')
