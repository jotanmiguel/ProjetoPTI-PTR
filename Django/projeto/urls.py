
from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('searchbar/', views.searchbar, name = 'searchbar'),
    path('produtos_list/', views.all_produtos, name="produtos_list"),
    path('base/',views.base, name="base"),
]
