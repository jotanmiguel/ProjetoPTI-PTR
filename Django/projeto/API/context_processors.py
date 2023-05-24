from .cart import Carrinho

def cart(request):
    return {'cart' : Carrinho(request)}

#Link do Swagger:_ http://127.0.0.1:8000/api/v1/swagger/schema