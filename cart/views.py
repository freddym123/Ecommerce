from django.shortcuts import render, get_object_or_404
from .cart import Cart
from base.models import Product
from django.http import JsonResponse
from django.core import serializers
# Create your views here.

def modal(request):
    cart = Cart(request)
    cart_products = cart.get_products()
    cart_products = serializers.serialize("json", cart_products)
    quantities = cart.get_quants()
    totals = cart.cart_total()
    items_total = cart.items_total()
    tax = float(totals)*.1
    subtotal = float(totals) + tax
    tax = f'{tax:.2f}'
    subtotal = f'{subtotal:.2f}'
    return JsonResponse({"cart_products": cart_products, "quantities": quantities, "totals": totals, "items_total": items_total, "tax": tax, "subtotal": subtotal})


def cart_summary(request):
    cart = Cart(request)
    cart_products = cart.get_products()
    quantities = cart.get_quants()
    totals = cart.cart_total()
    items_total = cart.items_total()
    tax = float(totals)*.1
    subtotal = float(totals) + tax
    tax = f'{tax:.2f}'
    subtotal = f'{subtotal:.2f}'
    print(items_total)
    return render(request, 'cart/cart.html', {"cart_products": cart_products, "quantities": quantities, "totals": totals, "items_total": items_total, "tax": tax, "subtotal": subtotal})

def cart_add(request):
    cart = Cart(request)

    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))
        product = get_object_or_404(Product, id=product_id)

        cart.add(product=product, quantity = product_qty)

        cart_quantity = cart.__len__()

        response = JsonResponse({'qty': cart_quantity})

        return response


def cart_delete(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        cart.delete(product=product_id)
        response = JsonResponse({'product': product_id})
        return response 

def cart_update(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))

        cart.update(product=product_id, quantity=product_qty)
        response = JsonResponse({'qty': product_qty})
        return response