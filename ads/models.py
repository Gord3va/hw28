from django.db import models


class Ads(models.Model):

    name = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    price = models.PositiveIntegerField(default=0)
    description = models.CharField(max_length=2000)
    address = models.CharField(max_length=100)
    is_published = models.CharField(max_length=6, default="None")

    def __str__(self):
        return self.name


class Categories(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
