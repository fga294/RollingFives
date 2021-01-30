from django.db import models
from tastypie.resources import ModelResource
from brasileirao.models import Team


# Create your models here.
class BrasileiraoResource(ModelResource):
    class Meta:
        queryset = Team.objects.all()
        resource_name = 'seriea'
        excludes = ['id']
