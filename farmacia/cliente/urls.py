from django.urls import path
from . import views

app_name='cliente'
urlpatterns = [    
    # Ruta que permite obtener y visualizar el listado de clientes registrados
    path('lista', views.lista, name='listaCliente'),
        
    # Ruta que permite agregar un nuevo cliente
    path('agregar', views.agregar, name='agregarCliente'),
    
    # Ruta que permite obtener el detalle del cliente seleccionado
    path('detalle/<int:id>', views.detalle, name='detalleCliente'),
    
    # Ruta que permite actualizar la información de un cliente seleccionado
    path('actualizar/<int:id>', views.actualizar, name='actualizarCliente'),
    
    # Ruta que permite eliminar la información de un cliente seleccionado
    path('eliminar/<int:id>', views.eliminar, name='eliminarCliente'),
]