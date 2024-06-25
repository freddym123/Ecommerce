from django.shortcuts import render
from .models import City
from . import forms
from cart.cart import Cart
# Create your views here.


def checkout(request):
    form = forms.ShippingForm()
    cart = Cart(request)
    cart_products = cart.get_products()
    quantities = cart.get_quants()
    totals = cart.cart_total()
    items_total = cart.items_total()
     
    tax = float(totals)*.1
    subtotal = float(totals) + tax
    tax = f'{tax:.2f}'
    subtotal = f'{subtotal:.2f}'

    return render(request, "payment/checkout.html", {'form': form, "products": cart_products, "quantities": quantities, "total": totals, "items_total": items_total, "tax": tax, "subtotal": subtotal})

def load_cities(request):
    country_id = request.GET.get('country_id')
    cities = City.objects.filter(country_id=country_id).all()
    return render(request, 'persons/city_dropdown_list_options.html', {'cities': cities})
    # return JsonResponse(list(cities.values('id', 'name')), safe=False)