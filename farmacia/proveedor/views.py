from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Proveedor
from .forms import AgregarProveedorForm, ActualizarProveedorForm

# Create your views here.
""" Este método permite visualizar el listado de proveedores """
@login_required
def ListarProveedores(request):
    listaProveedores = Proveedor.objects.order_by('id')
    
    return render(request, 'listaproveedor.html', {'listaProveedores':listaProveedores})

""" Este método permite agregar nuevos proveedores """
@login_required
def AgregarProveedor(request):
    if request.method=='POST':
        formProveedor = AgregarProveedorForm(request.POST)
        
        if formProveedor.is_valid():
            proveedor = Proveedor()
            proveedor.nombre = formProveedor.cleaned_data['nombre']
            proveedor.direccion = formProveedor.cleaned_data['direccion']
            proveedor.ciudad = formProveedor.cleaned_data['ciudad']
            proveedor.tipo_documento = formProveedor.cleaned_data['tipo_documento']
            proveedor.numero_documento = formProveedor.cleaned_data['numero_documento']
            proveedor.telefono = formProveedor.cleaned_data['telefono']
            proveedor.email = formProveedor.cleaned_data['email']
            proveedor.save()
            messages.add_message(request, messages.SUCCESS, 'Datos del proveedor almacenados.')
            return redirect('proveedor:listarproveedores')
    else:
        formProveedor =AgregarProveedorForm()
            
    return render(request, 'agregarproveedor.html', {'formProveedor': formProveedor})

""" Este método permite obtener el detalle del proveedor seleccionado """
@login_required
def DetalleProveedor(request, id):
    detalleproveedor = get_object_or_404(Proveedor, pk=id)
    return render(request, 'detalleproveedor.html', {'detalleproveedor':detalleproveedor})

""" Este método permite actualizar un proveedor seleccionado """
@login_required
def ActualizarProveedor(request, id):
    detalleproveedor = get_object_or_404(Proveedor, pk=id)
    if request.method=='POST':
        formProveedor = ActualizarProveedorForm(request.POST, instance=detalleproveedor)
        
        if formProveedor.is_valid():
            formProveedor.save()
            messages.add_message(request, messages.SUCCESS, 'Datos del cliente almacenados.')
            return redirect('proveedor:listarproveedores')
    else:
        formProveedor = ActualizarProveedorForm(instance=detalleproveedor)
            
    return render(request, 'actualizarproveedor.html', {'formProveedor':formProveedor, 'detalleproveedor':detalleproveedor})

""" Este método permite eliminar un cliente seleccionado """
@login_required
def EliminarProveedor(request, id):
    proveedor = get_object_or_404(Proveedor, pk=id)
    
    if proveedor:
        proveedor.delete()
    return redirect('proveedor:listarproveedores')