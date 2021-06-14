from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    
    path('iniciarSesion/', iniciarSesion, name="iniciarSesion"),

    path('listaClientes/', listaClientes, name="listaClientes"),

    path('eliminarCliente/<rut>', eliminarCliente, name="eliminarCliente"),

    path('modificarCliente/<rut>', modificarCliente, name="modificarCliente"),
    
    path('registroProducto/', registroProducto, name="registroProducto"),
    
    path('listaProductos/', listaProductos, name="listaProductos"),
    
    path('registroUsuario/', registroUsuario, name="registroUsuario"),

    
    path('registrarMarca/', registrarMarca, name="registrarMarca"),
    
    path('listaMarcas/', listaMarcas, name="listaMarcas"),
    
    path('modificarMarca/<id>/', modificarMarca, name="modificarMarca"),
    
    path('eliminarMarca/<id>/', eliminarMarca, name="eliminarMarca"),
    
    path('modificarProducto/<codigo_de_Barras>/', modificarProducto, 
    name="modificarProducto"),
    
    path('eliminarProducto/<codigo_de_Barras>/', eliminarProducto, 
    name="eliminarProducto")
    

]