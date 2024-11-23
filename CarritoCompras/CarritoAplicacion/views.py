from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm
from CarritoAplicacion.Carrito import Carrito
from CarritoAplicacion.models import Producto
from django.contrib.auth import authenticate, login,  logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

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

@login_required
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

@login_required
def agregarProducto(request, productoId):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=productoId)
    
    if producto.stock > 0:  # Solo agrega si hay stock disponible
        carrito.agregarProducto(producto)
        producto.stock -= 1  # Decrementa el stock
        producto.save()  # Guarda los cambios en el producto
    
    return redirect('Index')  # Redirigir al mismo index

@login_required
def eliminarProducto(request, productoId):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=productoId)
    carrito.eliminarProducto(producto)
    return redirect("Index")

@login_required
def restarProducto(request, productoId):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=productoId)
    
    if carrito.existeProducto(producto):  # Asegura que el producto esté en el carrito
        carrito.restar(producto)
        producto.stock += 1  # Incrementa el stock
        producto.save()  # Guarda los cambios en el producto
    
    return redirect("carritoVista")

@login_required
def sumarProducto(request, productoId):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=productoId)
    
    if producto.stock > 0:  # Solo agrega si hay stock disponible
        carrito.agregarProducto(producto)
        producto.stock -= 1  # Decrementa el stock
        producto.save()  # Guarda los cambios en el producto
    
    return redirect('carritoVista')

@login_required
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

from .models import Persona, Cliente

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  
            
            telefono = request.POST.get('telefono', '')


            cliente = Cliente.objects.create(user=user, telefono=telefono)
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1') 
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Te has registrado exitosamente y has iniciado sesión!')
                return redirect('Index')
    else:
        form = UserCreationForm()

    return render(request, 'auth/register.html', {'form': form})



def loginVista(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('Index') 
        else:
            messages.error(request, 'Nombre de usuario o contraseña incorrectos.')
            return render(request, 'auth/login.html')
    
    return render(request, 'auth/login.html')


def logout_user(request):
    logout(request)  
    return redirect('Index') 


@login_required
def checkout(request):
    carrito = Carrito(request)
    total_carrito = 0
    for item in carrito.carrito.values():
        total_carrito += item['precioFinal'] * item['stock']

    if total_carrito == 0:
        messages.error(request, "Tu carrito está vacío. Agrega productos antes de proceder al pago.")
        return redirect('Index')  
    
    return render(request, 'checkout.html', {'total': total_carrito})


@login_required
def procesar_pago(request):
    if request.method == 'POST':
        metodo_pago = request.POST.get('metodo_pago')
        procesador = ProcesadorPagos()
        cliente = Cliente.objects.get(user=request.user)

        if metodo_pago == 'efectivo':
            monto_recibido = float(request.POST.get('monto_recibido'))
            pago = Efectivo(monto_recibido=monto_recibido)
            if procesador.procesarPago(pago):
                factura = procesador.generarFactura(cliente)
                messages.success(request, f"Pago realizado exitosamente. Factura generada: {factura.id}")
                return redirect('Index')  
        
        elif metodo_pago == 'billetera_virtual':
            cuenta = request.POST.get('cuenta')
            pago = BilleteraVirtual(cuenta=cuenta)
            if procesador.procesarPago(pago):
                factura = procesador.generarFactura(cliente)
                messages.success(request, f"Pago realizado exitosamente. Factura generada: {factura.id}")
                return redirect('Index')

        elif metodo_pago == 'criptomonedas':
            wallet = request.POST.get('wallet')
            moneda = request.POST.get('moneda')
            pago = Criptomonedas(wallet=wallet, moneda=moneda)
            if procesador.procesarPago(pago):
                factura = procesador.generarFactura(cliente)
                messages.success(request, f"Pago realizado exitosamente. Factura generada: {factura.id}")
                return redirect('Index')

        elif metodo_pago == 'tarjeta_credito':
            numero_tarjeta = request.POST.get('numero_tarjeta')
            fecha_expiracion = request.POST.get('fecha_expiracion')
            pago = TarjetaCredito(numeroTarjeta=numero_tarjeta, fechaExpiracion=fecha_expiracion)
            if procesador.procesarPago(pago):
                factura = procesador.generarFactura(cliente)
                messages.success(request, f"Pago realizado exitosamente. Factura generada: {factura.id}")
                return redirect('Index')


        messages.error(request, "Hubo un error procesando el pago. Intenta nuevamente.")
        return redirect('Checkout')
    else:
        return redirect('Checkout')