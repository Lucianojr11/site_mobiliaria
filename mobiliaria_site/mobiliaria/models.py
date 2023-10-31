from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Imoveis(models.Model):
 
   address = models.CharField(max_length=200)
   status = models.TextField()
   area = models.TextField()
   bedrooms = models.TextField()
   bathrooms = models.TextField()
   floor = models.TextField()
   parking = models.TextField()
   value = models.TextField()
   type = models.TextField()
   path = models.ImageField()

class Message(models.Model):
   name = models.CharField(max_length=100 ,null=False, blank=False)
   email = models.EmailField()
   subject = models.TextField()
   message = models.TextField()
