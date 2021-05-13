from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from .forms import AgregarClienteForm, ActualizarClienteForm
from django.contrib import messages
from .models import Cliente

# Create your views here.
""" Este método permite visualizar el listado de Clientes """
@login_required
def lista(request):
    listaClientes = Cliente.objects.order_by('id')
    
    return render(request, 'lista.html', {'listaClientes':listaClientes})

""" Este método permite agregar nuevos Clientes """
@login_required
def agregar(request):
    if request.method=='POST':
        formCliente = AgregarClienteForm(request.POST)
        
        if formCliente.is_valid():
            cliente = Cliente()
            cliente.nombre = formCliente.cleaned_data['nombre']
            cliente.apellido = formCliente.cleaned_data['apellido']
            cliente.direccion = formCliente.cleaned_data['direccion']
            cliente.sexo = formCliente.cleaned_data['sexo']
            cliente.ciudad = formCliente.cleaned_data['ciudad']
            cliente.tipo_documento = formCliente.cleaned_data['tipo_documento']
            cliente.numero_documento = formCliente.cleaned_data['numero_documento']
            cliente.telefono = formCliente.cleaned_data['telefono']
            cliente.email = formCliente.cleaned_data['email']
            cliente.save()
            messages.add_message(request, messages.SUCCESS, 'Datos del cliente almacenados.')
            return redirect('cliente:listaCliente')
    else:
        formCliente =AgregarClienteForm()
            
    return render(request, 'agregar.html', {'formCliente': formCliente})

""" Este método permite obtener el detalle del cliente seleccionado """
def detalle(request, id):
    detallecliente = get_object_or_404(Cliente, pk=id)
    return render(request, 'detalle.html', {'detallecliente':detallecliente})

""" Este método permite agregar nuevos Clientes """
def actualizar(request, id):
    detallecliente = get_object_or_404(Cliente, pk=id)
    if request.method=='POST':
        formCliente = ActualizarClienteForm(request.POST, instance=detallecliente)
        
        if formCliente.is_valid():
            formCliente.save()
            messages.add_message(request, messages.SUCCESS, 'Datos del cliente almacenados.')
            return redirect('cliente:listaCliente')
    else:
        formCliente =ActualizarClienteForm(instance=detallecliente)
            
    return render(request, 'actualizar.html', {'formCliente': formCliente, 'detallecliente':detallecliente})

""" Este método permite agregar nuevos Clientes """
def eliminar(request, id):
    cliente = get_object_or_404(Cliente, pk=id)
    
    if cliente:
        cliente.delete()
    return redirect('cliente:listaCliente')