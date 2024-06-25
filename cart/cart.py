from base.models import Product
from base.models import User

class Cart():
    def __init__(self, request):
        self.session = request.session

        self.request = request

        cart = self.session.get("session_key")

        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        self.cart = cart

    def add(self, product, quantity):
        product_id = str(product.id)
        product_qty = str(quantity)

        if product_id in self.cart:
            pass
        else:
            self.cart[product_id] = {'price': str(product.price)}
            self.cart[product_id] = int(product_qty)
        
        self.session.modified = True

        if self.request.user.is_authenticated:
            current_user = User.objects.filter(id=self.request.user.id)
            cart_string = str(self.cart)
            cart_string = cart_string.replace("\'", "\"")
            current_user.update(old_cart = cart_string)


    def __len__(self):
        return len(self.cart)
    
    def get_products(self):
        product_ids = self.cart.keys()

        products = Product.objects.filter(id__in=product_ids)

        return products

    def get_quants(self):
        return self.cart
    
    def update(self, product, quantity):
        product_id = str(product)
        product_qty = int(quantity)

        ourcart = self.cart
        ourcart[product_id] = product_qty

        self.session.modified = True

        if self.request.user.is_authenticated:
            current_user = User.objects.filter(id=self.request.user.id)
            cart_string = str(self.cart)
            cart_string = cart_string.replace("\'", "\"")
            current_user.update(old_cart = cart_string)

        return self.cart
    
    def delete(self, product):
        product_id = str(product)

        if product_id in self.cart:
            del self.cart[product_id]

        self.session.modified = True

        if self.request.user.is_authenticated:
            current_user = User.objects.filter(id=self.request.user.id)
            cart_string = str(self.cart)
            cart_string = cart_string.replace("\'", "\"")
            current_user.update(old_cart = cart_string)
    
    def cart_total(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)


        qunatities = self.cart
        total = 0

        for key, value in qunatities.items():
            key = int(key)
            for product in products:
                if product.id == key:
                    if product.is_sale:
                        total + (product.sale_price * value)
                    else:
                        total = total + (product.price * value)

        return total
    
    def items_total(self):
        item_totals = {}
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)

        qunatities = self.cart

        for key, value in qunatities.items():
            key = int(key)
            for product in products:
                if product.id == key:
                    if product.is_sale:
                        item_totals[product.id] = value * product.sale_price
                    else:
                        item_totals[product.id] = value * product.price
        return item_totals
    
    def db_add(self, product, quantity):
        product_id = str(product)
        product_qty = str(quantity)

        if product_id in self.cart:
            pass
        else:
            #self.cart[product_id] = {'price': str(product.price)}
            self.cart[product_id] = int(product_qty)
        self.session.modified = True

        if self.request.user.is_authenticated:
            current_user = User.objects.filter(id=self.request.user.id)
            cart_string = str(self.cart)
            cart_string = cart_string.replace("\'", "\"")
            current_user.update(old_cart = cart_string)
    
    def get_tax(self):
        tax = 0
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        for key,value in self.cart:
            key = int(key)
            for product in products:
                if product.id == key:
                    if product.is_sale:
                        tax = (value * product.sale_price)*.1
                    else:
                        tax = (value * product.price)*.1
        return tax