from django.shortcuts import render, redirect
from .models import articulo, clientes
from TechnoStyleApp.forms import * 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

def inicio(request):
    return render(request, 'TechnoStyleApp/index.html')

def caracteristicas(request):
    return render(request, 'TechnoStyleApp/caracteristicas.html')

def agregar_producto(request):
    if request.method == "POST":
        miFormulario = FormularioAgregar(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            producto = articulo(marca=informacion["marca"], modelo=informacion["modelo"], categoria=informacion["categoria"], precio=informacion["precio"])
            producto.save()
            return render(request, "TechnoStyleApp/agregar-productos.html")
    else:
        miFormulario = FormularioAgregar()
    
    return render(request, "TechnoStyleApp/agregar-productos.html", {"miFormulario": miFormulario})

def agregar_cliente(request):
    if request.method == "POST":
        miFormulario = FormularioAgregarCliente(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            producto = clientes(nombre=informacion["nombre"], dni=informacion["dni"], correo=informacion["correo"], telefono=informacion["telefono"])
            producto.save()
            return render(request, "TechnoStyleApp/agregar_clientes.html")
    else:
        miFormulario = FormularioAgregarCliente()
    return render(request, "TechnoStyleApp/agregar_clientes.html", {"miFormulario": miFormulario})

def agregar_sucursal(request):
    if request.method == "POST":
        miFormulario = FormularioAgregarSucursal(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            producto = clientes(nombre=informacion["nombre"], numero_sucursal=informacion["numero_sucursal"], direccion=informacion["direccion"])
            producto.save()
            return render(request, "TechnoStyleApp/agregar_sucursales.html")
    else:
        miFormulario = FormularioAgregarSucursal()
    return render(request, "TechnoStyleApp/agregar_sucursales.html", {"miFormulario": miFormulario})

def buscar_productos(request):
    if request.method == "POST":
        miFormulario = BuscaProductos(request.POST)
        
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            producto = articulo.objects.filter(marca= informacion['marca'])
            return render(request,'TechnoStyleApp/lista_productos.html',{'producto': producto})
    else:
        miFormulario = BuscaProductos()
        return render(request, 'TechnoStyleApp/buscar_productos.html', {'miFormulario': miFormulario})

def registrarUsuario(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user=authenticate(username=username, password=password)
            login(request,user)
            return redirect('inicio')
    else:
        form = UserCreationForm()
        return render(request, 'registration/register.html', {'form': form})
