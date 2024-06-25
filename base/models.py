from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime
# Create your models here.


class User(AbstractUser):
    email = models.EmailField(max_length=200, unique=True)
    USERNAME_FIELD = 'email'
    username = models.TextField(unique=False)
    REQUIRED_FIELDS = []
    old_cart = models.CharField(max_length=200, blank=True, null=True)
    


    


class Category(models.Model):
    name: str = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.name

class Customer(models.Model):
    email = models.EmailField(max_length=100)

    def __str__(self) -> str:
        return f'{self.email}'

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=7)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    color = models.CharField(max_length=20)
    size = models.CharField(max_length=3)
    image = models.ImageField(upload_to='upload/product/')
    is_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(default=0, decimal_places=2, max_digits=7)

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default = 1) 
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    date = models.DateField(default=datetime.datetime.today)
    shipped = models.BooleanField(default = False)