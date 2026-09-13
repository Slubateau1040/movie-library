from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    platform = models.CharField(max_length=200)
    is_finished = models.BooleanField(default=False)
    rating = models.IntegerField(default=0)