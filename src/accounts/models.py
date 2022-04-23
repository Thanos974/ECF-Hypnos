from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class Custom_user(AbstractUser):
  last_name = models.CharField(max_length=100, blank=True)
  first_name = models.CharField(max_length=100, blank=True)
  email = models.EmailField(max_length=100, blank=True)
  password = models.CharField(max_length=100, blank=True)

  def __str__(self):
    return self.first_name


  
