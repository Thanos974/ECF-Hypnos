from django.db import models

# Create your models here.
class Booking(models.Model):
  hotel = models.CharField(max_length=50)
  suite =models.CharField(max_length=50)
  checkin = models.BooleanField(verbose_name="Arrivée")
  checkout = models.BooleanField(verbose_name="Départ")

  def __str__(self):
        return self.hotel and self.suite
