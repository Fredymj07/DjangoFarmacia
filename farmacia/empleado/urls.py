from django.urls import path
from . import views

app_name='empleado'
urlpatterns = [    
    # Ruta que permite obtener y visualizar el listado de clientes registrados
    path('ListarEmpleados/', views.ListarEmpleados, name='listarempleados'),
        
    # Ruta que permite agregar un nuevo cliente
    path('AgregarEmpleado/', views.AgregarEmpleado, name='agregarempleado'),
    
    # Ruta que permite obtener el detalle del cliente seleccionado
    path('DetalleEmpleado/<int:id>', views.DetalleEmpleado, name='detallempleado'),
    
    # Ruta que permite actualizar la información de un cliente seleccionado
    path('ActualizarEmpleado/<int:id>', views.ActualizarEmpleado, name='actualizarempleado'),
    
    # Ruta que permite eliminar la información de un cliente seleccionado
    path('EliminarEmpleado/<int:id>', views.EliminarEmpleado, name='eliminarempleado'),
]