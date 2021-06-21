from django.urls import path
from . import views

app_name='producto'
urlpatterns = [    
    # Ruta que permite obtener y visualizar el listado de clientes registrados
    path('ListarProductos/', views.ListarProductos, name='listarproductos'),
        
    # Ruta que permite agregar un nuevo cliente
    path('AgregarProducto/', views.AgregarProducto, name='agregarproducto'),
    
    # Ruta que permite obtener el detalle del cliente seleccionado
    path('DetalleProducto/<int:id>', views.DetalleProducto, name='detalleproducto'),
    
    # Ruta que permite actualizar la información de un cliente seleccionado
    path('ActualizarProducto/<int:id>', views.ActualizarProducto, name='actualizarproducto'),
    
    # Ruta que permite eliminar la información de un cliente seleccionado
    path('EliminarProducto/<int:id>', views.EliminarProducto, name='eliminarproducto'),
]