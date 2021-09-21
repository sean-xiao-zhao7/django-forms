from django.db import models

# Create your models here.

class Review(models.Model):
    name = models.CharField(max_length=100)
    review = models.TextField(max_length=500)
    rating = models.IntegerField()
