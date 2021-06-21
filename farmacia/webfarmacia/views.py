from django.shortcuts import render
from producto.models import Categoria, Producto

# Create your views here.
""" Este método permite visualizar la página principal de la farmacia """
def index(request):    
    categorias = Categoria.objects.order_by('id')
    return render(request, 'index.html', {'categorias':categorias})

""" Este método permite visualizar las categorías por producto """
# def FiltrarCategoriaProducto(request):
# def ListaCategorias(request):
#     categorias = Categoria.objects.order_by('id')
#     return render(request, 'index.html', {'categorias':categorias})