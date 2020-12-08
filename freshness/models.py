from django.db import models

# Create your models here.

class food(models.Model):
    item_no = models.CharField(max_length= 20)
    item = models.CharField(max_length= 20)
    description = models.CharField(max_length= 100)
    price= models.CharField(max_length= 20)
    temp = models.CharField(max_length= 20)
    humidity = models.CharField(max_length= 20)
    co2 = models.CharField(max_length = 20)
    o2 = models.CharField(max_length = 10)
    freshlevel = models.CharField(max_length = 20)