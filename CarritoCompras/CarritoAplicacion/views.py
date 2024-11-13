from django.shortcuts import render, HttpResponse, redirect
from CarritoAplicacion.Carrito import Carrito
from CarritoAplicacion.models import Producto

def index(request):
    # Crear una instancia del carrito
    carrito = Carrito(request)

    # Obtener el total de productos en el carrito
    total_productos = sum(item["stock"] for item in carrito.carrito.values())

    # Obtener el total del carrito usando el nuevo método
    total_carrito = carrito.calcular_total()

    # Obtener los productos disponibles
    productos = Producto.objects.all()

    return render(request, "index.html", {
        'productos': productos,
        'total_carrito': total_carrito,  # Pasamos el total al contexto
        'total_productos': total_productos,  # Pasamos el total de productos al contexto
    })

def carritoVista(request):
    # Obtener el carrito desde la sesión
    carrito = request.session.get('carrito', {})
    total_carrito = 0

    # Calcular el total del carrito
    for item in carrito.values():
        total_carrito += item['precioFinal'] * item['stock']

    # Pasar el carrito y el total a la plantilla
    return render(request, 'carritoVista.html', {
        'carrito': carrito,
        'total_carrito': total_carrito
    })


def agregarProducto(request, productoId):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=productoId)
    
    if producto.stock > 0:  # Solo agrega si hay stock disponible
        carrito.agregarProducto(producto)
        producto.stock -= 1  # Decrementa el stock
        producto.save()  # Guarda los cambios en el producto
    
    return redirect('Index')  # Redirigir al mismo index

def eliminarProducto(request, productoId):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=productoId)
    carrito.eliminarProducto(producto)
    return redirect("Index")

def restarProducto(request, productoId):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=productoId)
    
    if carrito.existeProducto(producto):  # Asegura que el producto esté en el carrito
        carrito.restar(producto)
        producto.stock += 1  # Incrementa el stock
        producto.save()  # Guarda los cambios en el producto
    
    return redirect("carritoVista")


def sumarProducto(request, productoId):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=productoId)
    
    if producto.stock > 0:  # Solo agrega si hay stock disponible
        carrito.agregarProducto(producto)
        producto.stock -= 1  # Decrementa el stock
        producto.save()  # Guarda los cambios en el producto
    
    return redirect('carritoVista')

def limpiarCarrito(request):
    carrito = Carrito(request)

    # Iterar sobre los productos en el carrito
    for item in carrito.carrito.values():
        # Verificar si el campo 'stockOriginal' está presente
        if 'stockOriginal' in item:
            producto = Producto.objects.get(id=item["productoId"])  # Obtenemos el producto por su ID
            stock_original = item["stockOriginal"]  # Obtenemos el stock original guardado en el carrito

            # Restauramos el stock al valor original
            producto.stock = stock_original
            producto.save()  # Guardamos los cambios en la base de datos
        else:
            print(f"ERROR: El producto {item['productoId']} no tiene 'stockOriginal'.")

    # Limpia el carrito (vacía la sesión)
    carrito.limpiarCarrito()

    return redirect("carritoVista")
