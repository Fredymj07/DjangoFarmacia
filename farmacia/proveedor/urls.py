from django.urls import path
from . import views

app_name='proveedor'
urlpatterns = [    
    # Ruta que permite obtener y visualizar el listado de clientes registrados
    path('ListarProveedores/', views.ListarProveedores, name='listarproveedores'),
        
    # Ruta que permite agregar un nuevo cliente
    path('AgregarProveedor/', views.AgregarProveedor, name='agregarproveedor'),
    
    # Ruta que permite obtener el detalle del cliente seleccionado
    path('DetalleProveedor/<int:id>', views.DetalleProveedor, name='detalleproveedor'),
    
    # Ruta que permite actualizar la información de un cliente seleccionado
    path('ActualizarProveedor/<int:id>', views.ActualizarProveedor, name='actualizarproveedor'),
    
    # Ruta que permite eliminar la información de un cliente seleccionado
    path('EliminarProveedor/<int:id>', views.EliminarProveedor, name='eliminarproveedor'),
]