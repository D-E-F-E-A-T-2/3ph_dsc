from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254, primary_key=True)
    password = models.CharField(max_length=10)
    datafile = models.FileField(blank=True)
