from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.dispatch import receiver


class ToDoList(models.Model):

    name = models.CharField(max_length=255, blank=False, unique=True)
    owner = models.ForeignKey('auth.User', related_name='todolists', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_altered = models.DateTimeField(auto_now=True)
    done = models.BooleanField(default=False)

    def __str__(self):
        """ Return user-friendly representation of the model instance"""
        return "{}".format(self.name)


@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)