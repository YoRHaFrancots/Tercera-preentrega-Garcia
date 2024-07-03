from django.urls import path, include
from .views import *

urlpatterns = [
  path('', home,name="home"),
   path('clientes/', clientes,name="clientes"),
   path('productos/', productos,name="productos"),
   path('pedidos/', pedidos,name="pedidos"),
  #forms
  path('productoForm/', productoForm,name="productoForm"),
  path('clienteForm/', clienteForm,name="clienteForm"),
  path('pedidoForm/', pedidoForm,name="pedidoForm"),
  path('buscarProductos/', buscarProductos,name="buscarProductos"),
  path('encontrarProductos/', encontrarProductos,name="encontrarProductos"),

]