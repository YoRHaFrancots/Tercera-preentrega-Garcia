from django.shortcuts import render
from .models import *
from .forms import *

def home(request):
    return render(request,"entidades/index.html")
def clientes(request):
    contexto={"clientes":Cliente.objects.all()}
    return render(request,"entidades/clientes.html",contexto)
def pedidos(request):
    contexto={"pedidos":Pedido.objects.all()}
    return render(request,"entidades/pedidos.html",contexto)
def productos(request):
    contexto={"productos":Producto.objects.all()}
    return render(request,"entidades/productos.html",contexto)

#formularios

def productoForm(request):
    if request.method == "POST":
        miForm=ProductoForm(request.POST)
        if miForm.is_valid():
            producto_nombre=miForm.cleaned_data.get("nombre")
            producto_precio=miForm.cleaned_data.get("precio")
            producto_stock=miForm.cleaned_data.get("stock")
            producto= Producto(nombre=producto_nombre,precio=producto_precio,stock=producto_stock)
            producto.save()
            contexto={"productos":Producto.objects.all()}
            return render(request,"entidades/productos.html",contexto)
       
    else:
        miForm = ProductoForm()
    
    return render(request, "entidades/productoForm.html", {"form": miForm})

def clienteForm(request):
    if request.method == "POST":
        miForm=ClienteForm(request.POST)
        if miForm.is_valid():
            cliente_nombre=miForm.cleaned_data.get("nombre")
            cliente_apellido=miForm.cleaned_data.get("apellido")
            cliente_email=miForm.cleaned_data.get("email")
            cliente= Cliente(nombre=cliente_nombre,apellido=cliente_apellido,email=cliente_email)
            cliente.save()
            contexto={"clientes":Cliente.objects.all()}
            return render(request,"entidades/clientes.html",contexto)
       
    else:
        miForm = ClienteForm()
    
    return render(request, "entidades/clienteForm.html", {"form": miForm})

def pedidoForm(request):
    if request.method == "POST":
        miForm=PedidoForm(request.POST)
        if miForm.is_valid():
            pedido_descripcion=miForm.cleaned_data.get("descripcion")
            pedido_direccion=miForm.cleaned_data.get("direccion")
            pedido_fechaEntrega=miForm.cleaned_data.get("fechaEntrega")
            pedido_entregado=miForm.cleaned_data.get("entregado")
            pedido= Pedido(descripcion=pedido_descripcion,direccion=pedido_direccion,fechaEntrega=pedido_fechaEntrega,entregado=False)
            pedido.save()
            contexto={"pedidos":Pedido.objects.all()}
            return render(request,"entidades/pedidos.html",contexto)
       
    else:
        miForm = PedidoForm()
    
    return render(request, "entidades/pedidoForm.html", {"form": miForm})

#Buscar producto
def buscarProductos(request):
    return render(request,"entidades/buscar.html")
def encontrarProductos(request):
    if request.GET["buscar"]:
        patron=request.GET["buscar"]
        productos=Producto.objects.filter(nombre__icontains=patron)
        contexto={"productos":productos}
    else:
        contexto={"productos":Producto.objects.all()}
        
    return render(request,"entidades/productos.html",contexto)
    