from django.shortcuts import render
from .models import Produto

# Create your views here.
def index(request):
    return render(request, 'index.html')

def searchbar(request):
    if request.method == "POST":
        searched = request.POST['searched']
        produtos = Produto.objects.filter(name__contains=searched)
        return render(request, 'searchbar.html',
        {'searched':searched,
        'produtos':produtos})
    else:
        return render(request, 'search.html', {})

def all_produtos(request):
    produtos_list = Produto.objects.all()
    return render(request, 'produtos_list.html',
    {'produtos_list':produtos_list})


def base(request):
    return render(request, 'base.html')