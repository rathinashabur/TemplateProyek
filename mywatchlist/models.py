from django.db import models

# Create your models here.
class WatchlistKu(models.Model):
    watched = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    rating = models.IntegerField()
    release_date = models.TextField()
    review = models.TextField()
