from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

User = get_user_model()

class Actor(models.Model):
    name = models.CharField(max_length=24)
    age = models.IntegerField()


class Movie(models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField(blank=True, null=True)
    release = models.DateField(default=timezone.now)
    actors = models.ManyToManyField(Actor, related_name='movie')
    poster = models.ImageField(upload_to='image/', blank=True)
    