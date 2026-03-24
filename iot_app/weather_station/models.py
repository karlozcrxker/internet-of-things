from django.db import models

# Create your models here.
class Sensors(models.Model):
    name= models.CharField(max_length=50)
    model= models.CharField(max_length=50)
