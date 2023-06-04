from django.shortcuts import render, get_object_or_404
from .models import Customer, Product, Order, Stock, Suplier, Cart, CartItem, Category, Review
from .serializers import CustomerSerializer, ProductSerializer, OrderSerializer, StockSerializer, SuplierSerializer, CategorySerializer, CartSerializer, CartItemSerializer, ReviewSerializer
from django.contrib.auth import login, logout
from .forms import PasswordChangingForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.contrib.auth.models import Group
from django.contrib import messages

from django.shortcuts import redirect
from rest_framework import generics
from django.template import loader
from django.http import HttpResponseRedirect
from django.urls import reverse
from rest_framework import permissions
from rest_framework import status
from rest_framework import views
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from . import serializers
from .cart import Carrinho
from django.contrib.auth.models import User
import requests
import json

from django.utils.text import slugify
from django.core.files.storage import FileSystemStorage

from rest_framework import status
from rest_framework.decorators import api_view
from django.views.decorators.csrf import requires_csrf_token
from rest_framework.response import Response


# Create your views here.
def index(request):
    products = Product.objects.all()
    if request.user.is_authenticated:
        username = request.user.username
    if request.user.groups.filter(name="Costumers"):
        customer = Customer.objects.get(name=username)
        try:
            if Order.objects.filter(customer=customer).exists():
                return render(request, 'index.html', {'products' : products})
            else:
                Order.objects.create(customer=customer)
        except:
            print("Erro")
    return render(request, 'index.html', {'products' : products})

def login(request):
    return render(request, 'login.html')


@api_view(['GET','POST'])
@requires_csrf_token
def registar(request):
    if request.method == "POST":
        name = request.POST.get("name") 
        email = request.POST.get("email")
        phone_number = request.POST.get("phone_number")
        password = request.POST.get("password")
        address = request.POST.get("address")
        zipCode = request.POST.get("zipCode")
        tipo = request.POST.get("type")

        clientes = Customer.objects.values_list("name", flat=True)
        fornecedores = Suplier.objects.values_list("name", flat=True)

        if name in clientes or name in fornecedores:
           return render(request, 'registar.html')
        else:
            if tipo=="Cliente":
                serializer = CustomerSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    user = User.objects.create_user(name, email, password)
                    user.save()
                    my_group = Group.objects.get(name='Costumers') 
                    my_group.user_set.add(user)
                    return render(request, 'registration_success.html')

            else:
                serializer = SuplierSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    user = User.objects.create_user(name, email, password)
                    user.save()
                    my_group = Group.objects.get(name='Supliers') 
                    my_group.user_set.add(user)
                    return render(request, 'registration_success.html')




    else:
        return render(request, 'registar.html')

    return render(request, 'index.html')

def shop(request):
    products = Product.objects.all()
    return render(request, 'shop.html', {'products' : products})

def product(request, slug):
    if request.user.is_authenticated:
        username = request.user.username
    product = Product.objects.get(slug=slug)
    if request.user.groups.filter(name="Costumers"):
        customer = Customer.objects.get(name=username)
        if request.method == "POST":
            o = Order.objects.get(customer=customer)
            o.products1.add(product)
                #o.products1.add(Product.objects.get(slug=slug))
    return render(request, 'product.html', {'product': product})

def add_to_cart(request, product_slug):
    cart = Carrinho(request)
    cart.add(product_slug)
    return render(request, 'menu_cart.html')

@api_view(['GET','POST'])
@requires_csrf_token
def adicionar_produto(request):
    if request.method == "POST":
        name = request.POST.get("name")
        category = request.POST.get("category")
        slug = request.POST.get("slug")
        image = request.FILES["image"]
        description = request.POST.get("description")
        price = request.POST.get("price")
        date = request.POST.get("proDate")
        produto = Product.objects.create(name=name, category=category, slug=slug, file=image, description=description, price=price, date=date)
        product_path = produto.file.path

        
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return render(request, "add_produto.html", {"product_path":product_path})
    return render(request, 'add_produto.html')

def conta(request):
    Suppliers = Suplier.objects.all()
    Customers = Customer.objects.all()
    return render(request,'conta.html', {"Suppliers":Suppliers,"Customers":Customers})

def eliminar_conta(request):
    if request.method == "POST":
        username = request.POST.get('name')
        clientes = Customer.objects.values_list("name", flat=True)
        fornecedores = Suplier.objects.values_list("name", flat=True)
        if username in clientes:
            cliente = Customer.objects.get(name = username)
            cliente.delete()
        if username in fornecedores:
            fornecedor = Suplier.objects.get(name = username)
            fornecedor.delete()
        try:
            u = User.objects.get(username = username)
            u.delete()
            messages.success(request, "The user is deleted")            

        except User.DoesNotExist:
            messages.error(request, "User does not exist")    
            return render(request, 'eliminar_conta.html')

        except Exception as e: 
            return render(request, 'eliminar_conta.html',{'err':e.message})
        return render(request,'index.html')

    return render(request, 'eliminar_conta.html')

def alterar_dados(request):
    if request.method == "POST":

        username = request.POST.get('name')

        phone_number = request.POST.get("phone_number")
        address = request.POST.get("address")
        zipCode = request.POST.get("zipCode")

        clientes = Customer.objects.values_list("name", flat=True)
        fornecedores = Suplier.objects.values_list("name", flat=True)

        if username in clientes:
            cliente = Customer.objects.get(name = username)
            cliente.phone_number = phone_number
            cliente.address = address
            cliente.zipCode = zipCode
            cliente.save()
        if username in fornecedores:
            fornecedor = Suplier.objects.get(name = username)
            fornecedor.phone_number = phone_number
            fornecedor.address = address
            fornecedor.zipCode = zipCode
            fornecedor.save()

        Suppliers = Suplier.objects.all()
        Customers = Customer.objects.all()
        return render(request,'conta.html', {"Suppliers":Suppliers,"Customers":Customers})
    
    Suppliers = Suplier.objects.all()
    Customers = Customer.objects.all()    
    return render(request,'alterar_dados.html', {"Suppliers":Suppliers,"Customers":Customers})

def registration_success(request):
    return render(request, 'registration_success.html')

def hist_encomendas(request):
    if request.user.is_authenticated:
        username = request.user.username
    if request.user.groups.filter(name="Costumers"):
        customer = Customer.objects.get(name=username)
        o = Order.objects.filter(customer=customer)
    #So para nao dar erros com suppliers, que ainda nao esta previsto encomendas do lado dos fornecedores
    else:
        supplier = Suplier.objects.filter(name=username)
        o = None
    return render(request,'historicoEncomendas.html',{'orders':o})

def login_success(request):
    return render(request, 'login_success.html')

def desporto(request):
    products = Product.objects.all()
    return render(request, 'desporto.html', {'products' : products})

def matEscritorio(request):
    products = Product.objects.all()
    return render(request, 'matEscritorio.html', {'products' : products})

def informatica(request):
    products = Product.objects.all()
    return render(request, 'informatica.html', {'products' : products})

def roupa(request):
    products = Product.objects.all()
    return render(request, 'roupa.html', {'products' : products})

def carrinho(request):
    if request.user.is_authenticated:
        username = request.user.username
    customer = Customer.objects.get(name=username)
    if not Order.objects.filter(customer=customer):
        Order.objects.create(customer=customer)
    o = Order.objects.get(customer=customer)
    if request.method == 'POST':
        order = Order.objects.get(id=o.id).delete()
        return render(request,'carrinho.html', {'orders': o})
    return render(request, 'carrinho.html',{'orders' : o})

def mPagamento(request):
    if request.user.is_authenticated:
        username = request.user.username
    customer = Customer.objects.get(name=username)
    if not Order.objects.filter(customer=customer):
        Order.objects.create(customer=customer)
    o = Order.objects.get(customer=customer)

    return render(request,'mPagamento.html',{'orders' : o})

def search(request):
    if request.method == "POST":
        searched = request.POST.get('searched')
        products = Product.objects.filter(name__contains=searched)
        return render(request, 'searchbar.html',
        {'searched':searched,
        'products':products})
    elif request.method == "GET":
        return render(request, 'searchbar.html', {})
    else:
        return render(request, 'search.html', {})

def base(request):
    return render(request, 'base.html')

def delete(request, id):
  product = Product.objects.get(id=id)
  if request.method == 'POST':
        # delete the band from the database
        product.delete()
        # redirect to the bands list
        return redirect('shop')

  return render(request, 'delete.html', {'product': product})

class CustomerList(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class StockList(generics.ListCreateAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

class StockDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

class SuplierList(generics.ListCreateAPIView):
    queryset = Suplier.objects.all()
    serializer_class = SuplierSerializer

class SuplierDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Suplier.objects.all()    
    serializer_class = SuplierSerializer
    
class CartList(generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    
class CartDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    
class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class LoginView(views.APIView):
    # This view should be accessible also for unauthenticated users.
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = serializers.LoginSerializer(data=self.request.data,
            context={ 'request': self.request })
        if serializer.is_valid():
            user = serializer.validated_data['user']
            login(request, user)
            return Response(None, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    success_url = reverse_lazy('password_success')

def password_success(request):
    return render(request, 'registration/password_success.html', {})