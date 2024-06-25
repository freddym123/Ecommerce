from django.urls import path
from . import views

urlpatterns = [
    path("", views.checkout, name="checkout"),
    path("load-cities", views.load_cities, name="load_cities"),
]