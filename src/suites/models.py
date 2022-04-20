from django.db import models


class Suite(models.Model):
    title = models.CharField(max_length=100, unique=True, verbose_name="Titre")
    description = models.CharField(max_length=400)
    thumbnail = models.ImageField(blank=True, verbose_name="Images")
    price = models.FloatField(max_length=6, verbose_name="Prix")

    def __str__(self):
       return self.name