from django.db import models

from main import settings


class Phone(models.Model):
    name = models.CharField(max_length=50)
    slug = models.CharField(max_length=50)
    image = models.ImageField()
    price = models.FloatField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()

    def __str__(self):
        return f'{self.name}, {self.release_date}: {self.price}'