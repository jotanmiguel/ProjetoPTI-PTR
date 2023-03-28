from django.shortcuts import render
from .models import Produto, Customer, Product, Order, Stock, Supplier
from .serializers import CustomerSerializer, ProductSerializer, OrderSerializer, StockSerializer, SupplierSerializer
from rest_framework import generics

# Create your views here.
def index(request):
    return render(request, 'index.html')

def search(request):
    if request.method == "POST":
        searched = request.POST.get('searched')
        produtos = Produto.objects.filter(name__contains=searched)
        return render(request, 'searchbar.html',
        {'searched':searched,
        'produtos':produtos})
    elif request.method == "GET":
        return render(request, 'searchbar.html', {})
    else:
        return render(request, 'search.html', {})

def all_produtos(request):
    produtos_list = Produto.objects.all()
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
    queryset = Produto.objects.all()
    serializer_class = ProductSerializer

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Produto.objects.all()
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

class SupplierList(generics.ListCreateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

class SupplierDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer