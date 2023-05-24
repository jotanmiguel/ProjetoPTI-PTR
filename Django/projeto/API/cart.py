from .models import Product
from django.conf import settings

class Carrinho(object):

    """
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)

        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        
        self.cart = cart
    
    def __iter__(self):
        for p in self.cart.keys():
            self.cart[str(p)]['product'] = Product.objects.get(pk=p)
    
    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())
    
    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True
    
    def add(self, product_slug, quantity=1, update_quantity=False):

        if product_slug not in self.cart:
            self.cart[product_slug] = {'quantity': 1, 'slug': product_slug}
        
        if update_quantity:
            self.cart[product_slug]['quantity'] += int(quantity)

            if self.cart[product_slug]['quantity'] == 0:
                self.remove(product_slug)
            
        self.save()
    
    def remove(self, product_slug):
        if product_slug in self.cart:
            del self.cart[product_slug]
            self.save()
    """