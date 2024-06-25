from django.db import models

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name
    
class OrderAddress(models.Model):
    fullname = models.CharField(max_length=100, null=False, blank=False)
    email = models.CharField(max_length=100, unique=False)
    address1 = models.CharField(max_length=100, null=False, blank=False)
    address2 = models.CharField(max_length=100, null=True, blank=True)
    zipcode = models.IntegerField(max_length=10, null=False, blank=False)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, blank=True, null=True)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, blank=True, null=True)
