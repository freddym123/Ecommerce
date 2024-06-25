from django.urls import path
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path("", views.Home, name="home"),
    path("products/", views.Products, name="products"),
    path("products/<str:cat>", views.Products, name="products"),
    path("product/<str:pk>", views.Product, name="product"),
    path('blog/', views.Blog, name="blog"),
    path('contact/', views.Contact, name="contact"),
    path('login/', views.Login, name="login"),
    path("logout/", views.Logout, name="logout"),
    path('register/', views.Register, name="register"),
]