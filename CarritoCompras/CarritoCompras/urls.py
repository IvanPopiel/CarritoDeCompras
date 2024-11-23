"""
URL configuration for CarritoCompras project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from CarritoAplicacion.views import index, carritoVista, agregarProducto, eliminarProducto, restarProducto, sumarProducto, limpiarCarrito, register, loginVista, logout_user, checkout


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="Index"), #incluyo para que levante el index
    path('carritoVista/', carritoVista, name="carritoVista"),
    path('agregar/<int:productoId>/', agregarProducto, name="Agregar"),
    path('eliminar/<int:productoId>/', eliminarProducto, name="Eliminar"),
    path('restar/<int:productoId>/', restarProducto, name="Restar"),
    path('sumar/<int:productoId>/', sumarProducto, name="Sumar"),
    path('impiar/', limpiarCarrito, name="Limpiar"),
    path('register/', register, name="Register"),
    path('login/', loginVista, name="Login"),
    path('logout/', logout_user, name='Logout'),
    path('checkout/', checkout, name='Checkout'),
    path('procesarPago/', checkout, name='ProcesarPago'),
]
