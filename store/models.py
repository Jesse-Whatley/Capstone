from django.db import models
import datetime
from django.contrib.auth import get_user_model

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/categories/', null=True, blank=True)
    
    def __str__(self):
        return self.name
    
    # Change name in app (Admin)
    class Meta:
        verbose_name_plural = "Categories"

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=1000)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    liked_by = models.ManyToManyField(get_user_model(), related_name='liked_products', blank=True)
    
    def __str__(self):
        return self.name

class Order(models.Model):
    name = models.CharField(max_length=255, blank=True)
    email = models.CharField(max_length=255, blank=True)
    street = models.CharField(max_length=200, blank=True)
    street_2 = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=200, blank=True)
    state = models.CharField(max_length=24, blank=True)
    zip_code = models.CharField(max_length=10, blank=True)
    phone = models.CharField(max_length=20, default='', blank=True)
    delivery_instructions = models.TextField(max_length=1000, blank=True)
    
    # auto fields
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)
    
    def __str__(self):
        return self.product