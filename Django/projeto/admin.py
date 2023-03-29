from django.contrib import admin
from .API.models import Product, Customer, Order, OrderProduct, Stock, Suplier, Category, Cart, CartItem, Review

# Register your models here.

# Objetos que tenham foreign key, devem ser registrados antes dos objetos que as utilizam
class ProductAdmin(admin.ModelAdmin):
    search_fields = ['name', 'name']
    readonly_fields = ['created_at', 'updated_at']
    raw_id_fields = ['suplier', 'category']
    
class categoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name', 'name']

admin.site.register(Product, ProductAdmin)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderProduct)
admin.site.register(Stock)
admin.site.register(Suplier)
admin.site.register(Category)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Review)
