from django.db import models

# Create your models here.


class Team(models.Model):
    name = models.CharField(max_length=255)
    year = models.IntegerField(default=2010)
    position = models.IntegerField(default=1)
    points = models.IntegerField(default=0)
