from django.shortcuts import render, get_object_or_404
from .models import Customer, Product, Order, Notifications, Stock, Suplier, Cart, CartItem, Category, Review
from .serializers import CustomerSerializer, ProductSerializer, OrderSerializer, StockSerializer, SuplierSerializer, CategorySerializer, CartSerializer, CartItemSerializer, ReviewSerializer
from django.contrib.auth import login, logout
from .forms import PasswordChangingForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.contrib.auth.models import Group
from django.contrib import messages
from django.contrib.auth.decorators import login_required

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
import datetime



from django.utils.text import slugify
from django.core.files.storage import FileSystemStorage

from rest_framework import status
from rest_framework.decorators import api_view
from django.views.decorators.csrf import requires_csrf_token
from rest_framework.response import Response


# Create your views here.
def index(request):
    products = Product.objects.all()
    numProds = len(products)
    if request.user.is_authenticated:
        username = request.user.username
    if request.user.groups.filter(name="Costumers"):
        customer = Customer.objects.get(name=username)
        try:
            if Order.objects.filter(customer=customer, status="Created").exists():
                return render(request, 'index.html', {'products' : products})
            else:
                Order.objects.create(customer=customer, status="Created")
        except:
            print("Erro")
    return render(request, 'index.html', {'products' : products, "numProds" : numProds})

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
        pwconf = request.POST.get("pwconf")
        address = request.POST.get("address")
        zipCode = request.POST.get("zipCode")
        tipo = request.POST.get("type")

        clientes = Customer.objects.values_list("name", flat=True)
        fornecedores = Suplier.objects.values_list("name", flat=True)

        if name in clientes or name in fornecedores:
           messages.info(request, 'Já existe um utilizador com este nome!')
           return render(request, 'registar.html')

        elif len(phone_number) != 9:
           messages.info(request, 'Número de telefone inválido!')
           return render(request, 'registar.html')

        elif pwconf != password:
           messages.info(request, 'As passwords não coincidem!')
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
            o = Order.objects.get(customer=customer, status="Created")
            o.products1.add(product)
                #o.products1.add(Product.objects.get(slug=slug))
    return render(request, 'product.html', {'product': product})

def add_to_cart(request, slug):
    cart = Carrinho(request)
    cart.add(slug)
    return render(request, 'menu_cart.html')

def teste(request):
    return render(request, 'teste.html')

def notificacoes(request):
    n = ''
    if request.user.is_authenticated:
        username = request.user.username
    if request.user.groups.filter(name="Supliers"):
        supplier = Suplier.objects.get(name=username)
        n = Notifications.objects.filter(supplier=supplier)
        print(supplier)
        print(supplier.id)
        print(n)

    return render(request, 'notificacoes.html',{'notifications':n})

def alterar_produto(request):
    slug = request.POST['slug']
    produto = Product.objects.get(slug=slug)
    if request.method == "POST":
        print(produto.description)
        descricao = request.POST.get('description')
        preco = request.POST.get('price')

        produto.description = descricao
        produto.price = preco
        produto.save()

    return render(request, 'alterar_produto.html',{'product':produto})

@api_view(['GET','POST'])
@requires_csrf_token
def adicionar_produto(request):

    today = str(datetime.date.today())

    if request.user.is_authenticated:
        username = request.user.username
    if request.user.groups.filter(name="Supliers"):
        supplier = Suplier.objects.get(name=username)
    if request.method == "POST":
        name = request.POST.get("name")
        category = request.POST.get("category")
        slug = request.POST.get("slug")
        try:
            image = request.FILES["image"]
        except:
            messages.info(request, 'O produto não tem imagem!')
            return render(request, 'add_produto.html')

        description = request.POST.get("description")
        price = request.POST.get("price")
        date = request.POST.get("proDate")
        if name == None or name == "":
            messages.info(request, 'O produto não tem nome!')
            return render(request, 'add_produto.html')
        elif description == None or description == "":
            messages.info(request, 'O produto não tem descrição!')
            return render(request, 'add_produto.html')
        elif price == None or price == "" or price == 0:
            messages.info(request, 'Preço Inválido!')
            return render(request, 'add_produto.html')
        else:
            produto = Product.objects.create(name=name, category=category, slug=slug, file=image, supplier=supplier, description=description, price=price, date=date)
            product_path = produto.file.path


            serializer = ProductSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
            return render(request, "add_success.html")
            #return render(request, "add_produto.html", {"product_path":product_path})

    return render(request, 'add_produto.html',{"today": today})

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
            if len(phone_number) != 9:
                messages.info(request, 'Número de telefone inválido!')
                return render(request, 'alterar_dados.html')
            cliente = Customer.objects.get(name = username)
            cliente.phone_number = phone_number
            cliente.address = address
            cliente.zipCode = zipCode
            cliente.save()
        elif username in fornecedores:
            if len(phone_number) != 9:
                messages.info(request, 'Número de telefone inválido!')
                return render(request, 'alterar_dados.html')
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

def add_success(request):
    return render(request, 'add_success.html')

def hist_encomendas(request):
    sOrders = []
    o = None
    if request.user.is_authenticated:
        username = request.user.username
    if request.user.groups.filter(name="Costumers"):
        customer = Customer.objects.get(name=username)
        o = Order.objects.filter(customer=customer)
    #So para nao dar erros com suppliers, que ainda nao esta previsto encomendas do lado dos fornecedores
    elif request.user.groups.filter(name="Supliers"):
        supplier = Suplier.objects.get(name=username)
        supProducts = Product.objects.filter(supplier=supplier)
        for product in supProducts:
            products = Order.objects.filter(products1=product)
            sOrders.append(products)

    return render(request,'historicoEncomendas.html',{'orders':o,'sOrders':sOrders})

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

def details(request, id):
    o = Order.objects.get(id=id)
    return render(request,'details.html',{'order':o})

@login_required(login_url='/accounts/login/')
def carrinho(request):
    if request.user.is_authenticated:
      username = request.user.username
      customer = Customer.objects.get(name=username)
    else:
      return render(request, 'accounts/login.html')
    if not Order.objects.filter(customer=customer, status="Created"):
        Order.objects.create(customer=customer, status="Created")
    o = Order.objects.get(customer=customer, status="Created")
    if request.method == 'POST':
        order = Order.objects.get(id=o.id).delete()
        return render(request,'carrinho.html', {'orders': o})
    return render(request, 'carrinho.html',{'orders' : o})

def mPagamento(request):
    if request.user.is_authenticated:
        username = request.user.username
    customer = Customer.objects.get(name=username)
    if not Order.objects.filter(customer=customer,status="Created"):
        Order.objects.create(customer=customer)
    o = Order.objects.get(customer=customer,status="Created")
    if request.method == "POST":
        o.status = "Paid"
        o.save()
        products = o.products1.all()
        for product in products:
            p = Product.objects.get(id=product.id)
            sup = p.supplier
            Notifications.objects.create(supplier=sup)

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
