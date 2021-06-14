from django import contrib
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.contrib import messages

# Create your views here.

def home(request):
    
    productos = Producto.objects.all()
    data = {
        'productos' : productos
    }
    
    return render(request, 'app/home.html', data)

def registroProducto(request):
    
    data = {
        'form' : RegProductoForm()
    }
    if request.method == 'POST':
        formulario = RegProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Producto Agregado Correctamente")
            return redirect(to=listaProductos)
        else:
            data["form"] = formulario

    return render(request, 'app/registroProducto.html', data)

def listaProductos(request):
    
    productos = Producto.objects.all().order_by("codigo_de_Barras")
    data = {
        'productos' : productos
    }
    
    return render(request, 'app/listaProductos.html', data)

def modificarProducto(request, codigo_de_Barras):
    
    producto = get_object_or_404(Producto, codigo_de_Barras = codigo_de_Barras)
    
    data = {
        'form' : ModProductoForm(instance=producto)
    }
    if request.method == 'POST':
        formulario = ModProductoForm(data=request.POST, instance=producto, files=request.FILES)

        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Producto Modificado Correctamente")
            return redirect(to=listaProductos)
        else:
            data["form"] = formulario
    
    return render(request, 'app/modificarProducto.html', data)

def eliminarProducto(request, codigo_de_Barras):
    
    producto = get_object_or_404(Producto, codigo_de_Barras = codigo_de_Barras)
    producto.delete()
    messages.success(request, "Producto Eliminado Correctamente")
    return redirect(to="listaProductos")
    
def registrarMarca(request):
    data = {
        'form' : RegMarcaForm()
    }
    if request.method == 'POST':
        formulario = RegMarcaForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Marca Agregada Correctamente")
            return redirect(to=listaMarcas)
        else:
            data["form"] = formulario
    return render(request, 'app/registrarMarca.html', data)

def modificarMarca(request, id):
    marca = get_object_or_404(Marca, id = id)
    
    data = {
        'form' : RegMarcaForm(instance=marca)
    }
    if request.method == 'POST':
        formulario = ModMarcaForm(data=request.POST, instance=marca)

        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Marca Modificada Correctamente")
            return redirect(to=listaMarcas)
        else:
            data["form"] = formulario
    
    return render(request, 'app/modificarMarca.html', data)

def listaMarcas(request):
    marcas = Marca.objects.all().order_by("id")
    data = {
        'marcas' : marcas
    }
    return render(request, 'app/listaMarcas.html', data)

def eliminarMarca(request, id):
    
    marca = get_object_or_404(Marca, id = id)
    marca.delete()
    messages.success(request, "Marca Eliminada Correctamente")
    return redirect(to=listaMarcas)

def registroUsuario(request):



    data = {
        'form' : RegUsuarioForm()
    }
    if request.method == 'POST':
        formulario = RegUsuarioForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Usuario Registrado Correctamente")
            return redirect(to=listaClientes)
        else:
            data["form"] = formulario

    return render(request, 'app/registroUsuario.html', data)

def iniciarSesion(request):

    return render(request, 'app/iniciarSesion.html')

def listaClientes(request):

    clientes = Usuario.objects.all().order_by("rut")

    data = {
        'clientes' : clientes
    }
    return render(request, 'app/listaClientes.html', data)

def eliminarCliente(request, rut):
    
    usuario = get_object_or_404(Usuario, rut = rut)
    usuario.delete()
    messages.success(request, "Usuario Eliminado Correctamente")
    return redirect(to=listaClientes)

def modificarCliente(request, rut):
    
    usuario = get_object_or_404(Usuario, rut = rut)
    
    data = {
        'form' : ModUsuarioForm(instance=usuario)
    }
    if request.method == 'POST':
        formulario = ModUsuarioForm(data=request.POST, instance=usuario)

        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Usuario Modificado Correctamente")
            return redirect(to=listaClientes)
        else:
            data["form"] = formulario
    
    return render(request, 'app/modificarCliente.html', data)