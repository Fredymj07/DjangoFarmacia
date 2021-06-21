from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Empleado
from .forms import ActualizarEmpleadoForm, AgregarEmpleadoForm

# Create your views here.
""" Este método permite visualizar el listado de empleados """
@login_required
def ListarEmpleados(request):
    listaEmpleados = Empleado.objects.order_by('id')
    
    return render(request, 'listaempleado.html', {'listaEmpleados':listaEmpleados})

""" Este método permite agregar nuevos empleados """
@login_required
def AgregarEmpleado(request):
    if request.method=='POST':
        formEmpleado = AgregarEmpleadoForm(request.POST)
        
        if formEmpleado.is_valid():
            empleado = Empleado()
            empleado.nombre = formEmpleado.cleaned_data['nombre']
            empleado.apellido = formEmpleado.cleaned_data['apellido']
            empleado.direccion = formEmpleado.cleaned_data['direccion']
            empleado.sexo = formEmpleado.cleaned_data['sexo']
            empleado.ciudad = formEmpleado.cleaned_data['ciudad']
            empleado.tipo_documento = formEmpleado.cleaned_data['tipo_documento']
            empleado.numero_documento = formEmpleado.cleaned_data['numero_documento']
            empleado.telefono = formEmpleado.cleaned_data['telefono']
            empleado.email = formEmpleado.cleaned_data['email']
            empleado.save()
            messages.add_message(request, messages.SUCCESS, 'Datos del empleado almacenados.')
            return redirect('empleado:listarempleados')
    else:
        formEmpleado =AgregarEmpleadoForm()
            
    return render(request, 'agregarempleado.html', {'formEmpleado': formEmpleado})

""" Este método permite obtener el detalle del empleado seleccionado """
@login_required
def DetalleEmpleado(request, id):
    detallempleado = get_object_or_404(Empleado, pk=id)
    return render(request, 'detallempleado.html', {'detallempleado':detallempleado})

""" Este método permite actualizar un empleado seleccionado """
@login_required
def ActualizarEmpleado(request, id):
    detallempleado = get_object_or_404(Empleado, pk=id)
    if request.method=='POST':
        formEmpleado = ActualizarEmpleadoForm(request.POST, instance=detallempleado)
        
        if formEmpleado.is_valid():
            formEmpleado.save()
            messages.add_message(request, messages.SUCCESS, 'Datos del cliente almacenados.')
            return redirect('empleado:listarempleados')
    else:
        formEmpleado = ActualizarEmpleadoForm(instance=detallempleado)
            
    return render(request, 'actualizarempleado.html', {'formEmpleado':formEmpleado, 'detallempleado':detallempleado})

""" Este método permite eliminar un empleado seleccionado """
@login_required
def EliminarEmpleado(request, id):
    empleado = get_object_or_404(Empleado, pk=id)
    
    if empleado:
        empleado.delete()
    return redirect('empleado:listarempleados')