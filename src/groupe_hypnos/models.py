from django.db import models

# Create your models here.

class Hotel(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Nom")
    description = models.CharField(max_length=400)
    address = models.CharField(max_length=100, verbose_name="adresse")
    zip_code = models.CharField(max_length=5, verbose_name="Code postal")
    city = models.CharField(max_length=100, verbose_name="Ville")

    def __str__(self):
        return self.name


class Suite(models.Model):
    title = models.CharField(max_length=100, unique=True, verbose_name="")
    description = models.CharField(max_length=400)
    price = models.FloatField(max_length=6, verbose_name="prix")