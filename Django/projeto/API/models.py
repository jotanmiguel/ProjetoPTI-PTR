from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Produto(models.Model):
	name = models.CharField('Nome do produto', max_length=1000)
	price = models.CharField('Preço do produto', max_length=10)
	#code = models.TextField()
	#img = models.ImageField(upload_to = "images/")
	#file = models.FileField(upload_to = "files/")
	#slug = models.SlugField(max_length=1000)
	#category = models.CharField(max_length=500)
	#Author = models.CharField(max_length=500)
	date = models.DateTimeField('Data de produção')

	def __str__(self):
		return self.name

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=200, blank=True)

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    supplier = models.ForeignKey('Supplier', on_delete=models.CASCADE)

class Order(models.Model):
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='OrderProduct')
    status = models.CharField(max_length=50, default='Created')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class OrderProduct(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.IntegerField()

class Stock(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    location = models.CharField(max_length=200)
    updated_at = models.DateTimeField(auto_now=True)

class Supplier(models.Model):
    name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20, blank=True)
    email = models.EmailField(max_length=254, blank=True)
    address = models.CharField(max_length=200, blank=True)