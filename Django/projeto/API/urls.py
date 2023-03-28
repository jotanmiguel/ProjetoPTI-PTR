
from django.contrib import admin
from django.urls import include, path
from .views import index, search, all_produtos, base, CustomerList, CustomerDetail, ProductList, ProductDetail, OrderList, OrderDetail, StockList, StockDetail

urlpatterns = [
    path('', index, name="index"),
    path('search/', search, name = 'search'),
    path('produtos_list/', all_produtos, name="produtos_list"),
    path('base/',base, name="base"),
    path('customers/', CustomerList.as_view(), name='customer-list'),
    path('customers/<int:pk>/', CustomerDetail.as_view(), name='customer-detail'),
    path('products/', ProductList.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetail.as_view(), name='product-detail'),
    path('orders/', OrderList.as_view(), name='order-list'),
    path('orders/<int:pk>/', OrderDetail.as_view(), name='order-detail'),
    path('stocks/', StockList.as_view(), name='stock-list'),
    path('stocks/<int:pk', StockDetail.as_view(), name='stock-detail'),
]
