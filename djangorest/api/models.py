from django.db import models

class ToDoList(models.Model):

    name = models.CharField(max_length=255, blank=False, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_altered = models.DateTimeField(auto_now=True)
    done = models.BooleanField(default=False)

    def __str__(self):
        """ Return user-friendly representation of the model instance"""
        return "{}".format(self.name)
