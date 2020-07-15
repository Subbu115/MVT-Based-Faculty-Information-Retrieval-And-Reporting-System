from django.db import models

# Create your models here.

class Department(models.Model):

    name = models.CharField(max_length=100)
    acronym = models.CharField(max_length=10)
    code = models.CharField(max_length=100)
    estd = models.DateTimeField()
    location = models.CharField(max_length=100)
