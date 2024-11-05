from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
from CarritoAplicacion.Carrito import Carrito
from CarritoAplicacion.models import Producto
def index(request):
    #render para cargar el index.html
    productos = Producto.objects.all()
    return render(request, "index.html", {'productos':productos}) #recupera todos nuestros objetos guardados en la BBDD

def agregarProducto(request, productoId):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=productoId)
    carrito.agregarProducto(producto)
    return redirect("Index")

def eliminarProducto(request, productoId):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=productoId)
    carrito.eliminarProducto(producto)
    return redirect("Index")

def restarProducto(request, productoId): 
    carrito = Carrito(request)
    producto = Producto.objects.get(id=productoId)
    carrito.restar(producto)
    return redirect("Index")

def limpiarCarrito(request):
    carrito = Carrito(request)
    carrito.limpiarCarrito()
    return redirect("Index")