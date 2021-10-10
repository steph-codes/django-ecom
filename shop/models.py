from django.db import models
from django.db import models

# Create your models here.
#guess the properties/details u want to save in ur Product /class e.g title,desc,image,price

class Products(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    discount_price = models.FloatField()
    category = models.CharField(max_length=200)
    description = models.TextField()
    image = models.CharField(max_length=300)

