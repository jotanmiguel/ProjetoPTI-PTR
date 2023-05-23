from django.db import models
import uuid

# Create your models here.
# Clientes
class Customer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=200, blank=True)
    email = models.EmailField(max_length=254, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=200, blank=True)
    zipCode = models.CharField(max_length=200, blank=True)
    password = models.CharField(max_length=200, blank=True) 
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)     
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)   

    def __str__(self):
        return self.name

# Produtos
class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    file = models.FileField()
    #suplier = models.ForeignKey('Suplier', on_delete=models.CASCADE)
    #category = models.ForeignKey('Category', on_delete=models.CASCADE)
    date = models.DateField(auto_now_add = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
# Pedidos de produtos
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='OrderProduct')
    status = models.CharField(max_length=50, default='Created')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

# Inventário de produtos
class Stock(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    location = models.CharField(max_length=200)
    updated_at = models.DateTimeField(auto_now=True)
 
# Categorias de produtos    
class Category(models.Model):
    name = models.CharField(max_length=255)
    parent_category = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.name
    
    def get_children(self):
        return Category.objects.filter(parent_category=self)

# Fornecedores de produtos
class Suplier(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200, blank=True)
    email = models.EmailField(max_length=254, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=200, blank=True)
    zipCode = models.CharField(max_length=200, blank=True)
    password = models.CharField(max_length=200, blank=True) 
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)     
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)   

    def __str__(self):
        return self.name
    
# Carrinho de compras
class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class CartItem(models.Model):
    cart = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
# Avaliações de produtos
class Review(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(default=1)
    comment = models.TextField(max_length=500, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class ProductionUnit(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    email = models.EmailField(max_length=254, blank=True)
    owner = models.ForeignKey("ProductionUnit", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
