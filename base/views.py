from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db.models import Q
from . import models
import json
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from cart.cart import Cart

# Create your views here.

def Home(request):
    our_picks = models.Product.objects.all()
    context = {'home': 'active', "our_picks": our_picks}
    return render(request, 'base/home.html', context)

def Product(request, pk):
    product = models.Product.objects.get(id=pk)

    context = {'product': product}
    return render(request, "base/product.html", context)

def Products(request, cat = ''):
    q = request.GET.get('q')
    if q != None:
        products = models.Product.objects.filter(Q(name__icontains = q))
        return render(request, 'base/product_query.html', {"productss": "active", "products": products, "q": q})

    products = None
    if cat == '':
        products = models.Product.objects.all()  
    else:
        category = models.Category.objects.get(name=cat)
        products = models.Product.objects.filter(category = category)
    cat = cat.replace(' ', '_')
    print(products)
    context = {'productss': 'active', 'products': products, f'{cat}': 'viewing'}
    return render(request, "base/products.html", context)

def Blog(request):
    context = {'blog': 'active'}
    return render(request, 'base/blog.html', context)

def Contact(request):
    context = {'contact': 'active'}
    return render(request, 'base/contact.html', context)

def Login(request):

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        email = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)

            current_user = models.User.objects.get(id=request.user.id)
            saved_cart = current_user.old_cart

            if saved_cart:
                converted_cart = json.loads(saved_cart)

                cart = Cart(request)
                for key, value in converted_cart.items():
                    cart.db_add(product=key, quantity=value)


            messages.success(request, ("Logged In"))
            return redirect('home')
        else:
            form = CustomAuthenticationForm()
    else:
        form = CustomAuthenticationForm()
    
    return render(request, 'base/login.html', {'form': form})

def Logout(request):
    logout(request)
    messages.success(request, ("You have been logged out"))
    return redirect('home')

def Register(request):
    form = CustomUserCreationForm()
    error_messages = []
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)

        print(form.data)
        for field in form:
            print("Field Error: ", field.name, field.errors)
        if form.is_valid():
            form.save()
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password1"]
            password2 = form.cleaned_data["password2"]

            user = authenticate(username=email, password=password)
            login(request, user)
            return redirect("home")
        else:
            password = form.cleaned_data["password1"]
            password2 = form.cleaned_data["password2"]
            form = CustomUserCreationForm(request.POST)
            if password != password2:
                error_messages = ["Passwords don't match"]
            else:
                error_messages = ["Your password must contain at least 8 characters",
                       "Your password can't be a commonly used password",
                       "Your password can't be entirely numeric"]
            
            
    return render(request, 'base/register.html', {'form': form, "error_messages": error_messages})