from django.shortcuts import render
from .models import Customer, Product, Order, Stock, Suplier, Cart, CartItem, Category, Review
from .serializers import CustomerSerializer, ProductSerializer, OrderSerializer, StockSerializer, SuplierSerializer, OrderProductSerializer, CategorySerializer, CartSerializer, CartItemSerializer, ReviewSerializer
from django.contrib.auth import login, logout

from rest_framework import generics
from django.http import HttpResponseRedirect
from django.urls import reverse
from rest_framework import permissions
from rest_framework import status
from rest_framework import views
from rest_framework.response import Response
from . import serializers
from django.contrib.auth.models import User
import requests
import json

from rest_framework import status
from rest_framework.decorators import api_view
from django.views.decorators.csrf import requires_csrf_token
from rest_framework.response import Response



# Create your views here.
def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

@api_view(['GET','POST'])
@requires_csrf_token
def registar(request):
    if request.method == "POST":
        name = request.POST.get("name") 
        email = request.POST.get("email")
        password = request.POST.get("password")
        address = request.POST.get("address")
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

            else:
                serializer = CustomerSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()


            user = User.objects.create_user(name, email, password)
            user.save()

    else:
        return render(request, 'registar.html')

    return render(request, 'index.html')


def carrinho(request):
    return render(request, 'carrinho.html')

def mPagamento(request):
    return render(request, 'mPagamento.html')

def search(request):
    if request.method == "POST":
        searched = request.POST.get('searched')
        produtos = Product.objects.filter(name__contains=searched)
        return render(request, 'searchbar.html',
        {'searched':searched,
        'produtos':produtos})
    elif request.method == "GET":
        return render(request, 'searchbar.html', {})
    else:
        return render(request, 'search.html', {})

def all_produtos(request):
    produtos_list = Product.objects.all()
    return render(request, 'produtos_list.html',
    {'produtos_list':produtos_list})

def base(request):
    return render(request, 'base.html')


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
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return Response(None, status=status.HTTP_202_ACCEPTED)
