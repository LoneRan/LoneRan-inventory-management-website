from django.db import models

# Create your models here.

class food(models.Model):
    item_no = models.DecimalField(max_digits = 10, decimal_places = 0,unique=True)
    item = models.CharField(max_length= 20, unique=True)
    description = models.CharField(max_length= 100)
    price= models.DecimalField(max_digits = 10, decimal_places = 2)
    temp = models.DecimalField(max_digits = 10, decimal_places = 0)
    humidity = models.DecimalField(max_digits = 10, decimal_places = 0)
    co2 = models.CharField(max_length = 20)
    o2 = models.CharField(max_length = 10)
    freshlevel = models.CharField(max_length = 20)