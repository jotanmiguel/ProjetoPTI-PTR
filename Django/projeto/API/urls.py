
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path
from .views import index, search, alterar_dados, login, registar, shop, product, add_to_cart, adicionar_produto, conta, eliminar_conta, hist_encomendas, PasswordsChangeView, password_success, login_success, registration_success, desporto, matEscritorio, informatica, roupa, carrinho, mPagamento, base, delete, CustomerList, CustomerDetail, ProductList, ProductDetail, OrderList, OrderDetail, StockList, StockDetail, CartList, CartDetail, SuplierList, SuplierDetail, CategoryDetail, CategoryList
from . import views



urlpatterns = [
    path('', index, name="index"),
    path('search/', search, name = 'search'),
    #path('login/', views.LoginView.as_view()),
    path('accounts/', include("django.contrib.auth.urls")),
    path('login/', login, name = 'login'),
    path('registar/', registar, name='registar'),
    path('shop/', shop, name='shop'),
    path('product/', product, name='product'),
    path('shop/<slug:slug>/', product, name='product'),
    path('shop/<category:category/', product, name='product'),
    path('add_to_cart/<slug:slug>/', add_to_cart, name='add_to_cart'),
    path('adicionar_produto/', adicionar_produto, name='adicionar_produto'),
    path('conta', conta, name='conta'),
    path('password/', PasswordsChangeView.as_view(template_name='registration/change-password.html')),
    path('registration_success/', registration_success, name='registration_success'),
    path('login_success/', login_success, name='login_success'),
    path('password_success', password_success, name="password_success"),
    path('desporto', desporto, name='desporto'),
    path('materialEscritorio', matEscritorio, name='matEscritorio'),
    path('informatica', informatica, name='informatica'),
    path('roupa', roupa, name='roupa'),
    path('carrinho/', carrinho, name='carrinho'),
    path('pagamento/', mPagamento, name='mPagamento'),
    path('base/',base, name="base"),
    path('eliminar_conta', eliminar_conta, name="eliminar_conta"),
    path('historico', hist_encomendas, name="historico"),
    path('delete/<str:id>', delete, name='delete'),
    path('customers/', CustomerList.as_view(), name='customer-list'),
    path('customers/<str:pk>/', CustomerDetail.as_view(), name='customer-detail'),
    path('products/', ProductList.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetail.as_view(), name='product-detail'),
    path('orders/', OrderList.as_view(), name='order-list'),
    path('orders/<int:pk>/', OrderDetail.as_view(), name='order-detail'),
    path('stocks/', StockList.as_view(), name='stock-list'),
    path('stocks/<int:pk>', StockDetail.as_view(), name='stock-detail'),
    path('supliers/', SuplierList.as_view(), name='supplier-list'),
    path('supliers/<int:pk>', SuplierDetail.as_view(), name='supplier-detail'),
    path('carts/', CartList.as_view(), name='cart-list'),
    path('carts/<int:pk>', CartDetail.as_view(), name='cart-detail'),
    path('categories/', CategoryList.as_view(), name='category-list'),
    path('categories/<int:pk>', CategoryDetail.as_view(), name='category-detail'),
    path('alterar_dados/', alterar_dados ,name="alterar_dados")
]
