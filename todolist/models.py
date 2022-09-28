from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User,
                models.SET_NULL,
                blank=True,
                null=True)
    date = models.DateField()
    title = models.CharField(max_length=100)
    description = models.TextField()