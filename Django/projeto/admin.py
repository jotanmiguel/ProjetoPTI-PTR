from django.contrib import admin
from .API.models import Produto, Customer, Order, OrderProduct, Stock, User, Supplier
# Register your models here.

admin.site.register(Produto)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderProduct)
admin.site.register(Stock)
admin.site.register(Supplier)