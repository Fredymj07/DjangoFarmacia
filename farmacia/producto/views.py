from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Producto
from .forms import AgregarProductoForm, ActualizarProductoForm
from bootstrap_datepicker_plus import DatePickerInput

# Create your views here.
""" Este método permite visualizar el listado de productos """
@login_required
def ListarProductos(request):
    listaProductos = Producto.objects.order_by('id')
    
    return render(request, 'listaproducto.html', {'listaProductos':listaProductos})

""" Este método permite agregar nuevos productos """
@login_required
def AgregarProducto(request):
    if request.method=='POST':
        formProducto = AgregarProductoForm(request.POST, request.FILES)
        
        if formProducto.is_valid():
            producto = Producto()
            producto.nombre = formProducto.cleaned_data['nombre']
            producto.cantidad_disponible = formProducto.cleaned_data['cantidad_disponible']
            producto.fecha_vencimiento = formProducto.cleaned_data['fecha_vencimiento']
            producto.categoria = formProducto.cleaned_data['categoria']
            producto.proveedor = formProducto.cleaned_data['proveedor']
            producto.descripcion = formProducto.cleaned_data['descripcion']
            producto.imagen = formProducto.cleaned_data['imagen']
            producto.save()
            messages.add_message(request, messages.SUCCESS, 'Datos del producto almacenados.')
            return redirect('producto:listarproductos')
    else:
        formProducto =AgregarProductoForm()
            
    return render(request, 'agregarproducto.html', {'formProducto': formProducto})

""" Este método permite obtener el detalle de un producto seleccionado """
@login_required
def DetalleProducto(request, id):
    detalleproducto = get_object_or_404(Producto, pk=id)
    return render(request, 'detalleproducto.html', {'detalleproducto':detalleproducto})

""" Este método permite actualizar un producto seleccionado """
@login_required
def ActualizarProducto(request, id):
    detalleproducto = get_object_or_404(Producto, pk=id)
    if request.method=='POST':
        formProducto = ActualizarProductoForm(request.POST, request.FILES, instance=detalleproducto)
        
        if formProducto.is_valid():
            formProducto.save()
            messages.add_message(request, messages.SUCCESS, 'Datos del producto almacenados.')
            return redirect('producto:listarproductos')
    else:
        formProducto = ActualizarProductoForm(instance=detalleproducto)
            
    return render(request, 'actualizarproducto.html', {'formProducto':formProducto, 'detalleproducto':detalleproducto})

""" Este método permite eliminar un producto seleccionado """
@login_required
def EliminarProducto(request, id):
    producto = get_object_or_404(Producto, pk=id)
    
    if producto:
        producto.delete()
    return redirect('producto:listarproductos')