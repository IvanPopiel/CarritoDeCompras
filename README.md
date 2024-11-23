# Proyecto: Carrito de Compras en Django


## Descripción del Proyecto

Este proyecto consiste en el desarrollo de un sistema de carrito de compras en línea, diseñado para facilitar la inscripción a cursos a través de una interfaz web moderna y funcional.  
Implementado en **Python** con el framework **Django**, el sistema incorpora características esenciales como:

- Navegación de productos.
- Gestión de carrito.
- Confirmación de pedidos.

El sistema integra principios de **programación orientada a objetos** tales como **herencia**, **polimorfismo** y **encapsulamiento**, así como el uso de **patrones de diseño**.  
El enfoque principal está en ofrecer una experiencia de usuario fluida y eficiente mediante una interfaz ideal tanto para usuarios de escritorio como para dispositivos móviles. Además, incluye funcionalidades administrativas que permiten gestionar el inventario de manera simple y eficaz.

---

## Contexto y Propósito del Proyecto

Este proyecto busca atender la necesidad de pequeños y medianos negocios de contar con una herramienta accesible para vender sus cursos de manera digital.  
El propósito principal es:

- Crear una base tecnológica sólida que pueda ampliarse en el futuro para incluir:
  - Integraciones como sistemas de envío.
  - Pasarelas de pago.
  - Análisis avanzados de datos.

Además, este proyecto representa una oportunidad para que el equipo adquiera experiencia práctica en desarrollo web, diseño orientado a objetos y trabajo colaborativo.

---

## Equipo del Proyecto

- **Juan Carbajal**  
- **Santiago Falcón**  
- **Iván Popiel**  
- **Nahuel Ramallo**




## JIRA del proyecto
[JIRA del proyecto](https://ezequiel-grisoski.atlassian.net/jira/software/projects/CAC/boards/3)

## Objetivo del Proyecto

Crear un sistema de carrito de compras funcional implementado en Python con el framework Django, para su navegación web. Este sistema busca proporcionar a los usuarios una experiencia de compra fluida, desde la navegación de productos hasta la confirmación de pedidos. 

El sistema permitirá a los usuarios explorar productos, agregar ítems al carrito y realizar compras. Los administradores podrán gestionar el inventario de productos y modificar la base de datos.

El proyecto también está diseñado para ser escalable, facilitando la integración futura con pasarelas de pago, funciones de pago, recomendaciones de productos o historial de compras.

---

## Alcance

### Para usuarios:
1. Navegar listado de productos.
2. Visualizar detalles de los productos, incluyendo descripción, precio y disponibilidad.
3. Crear y gestionar un carrito de compras con opciones para agregar o quitar productos.
4. Confirmar compras y recibir detalles de los productos seleccionados y el total.

### Para administradores:
1. Gestionar el inventario: alta, baja y actualización de productos.
2. Monitorear los pedidos confirmados y asegurar la disponibilidad del stock.
3. Acceder a una interfaz simplificada para realizar modificaciones rápidas en el sistema.

---

## Límites del Sistema

### Incluido:
1. **Gestión de productos:** Alta, baja, modificación y consulta de productos disponibles en la base de datos.
2. **Carrito de compras:** Funciones de agregar, eliminar productos y calcular totales en tiempo real.
3. **Interfaz de usuario:** Página web que garantiza simplicidad y rapidez en las operaciones.
4. **Seguridad básica:** Validación de formularios.

### Excluido:
1. Gestión de envíos: no incluye seguimiento ni cálculo de costos de envío.
2. Integración con múltiples pasarelas de pago: los pagos son simulados.
3. Reportes avanzados: estadísticas de ventas o reportes de inventario.
4. Multilenguaje: solo estará disponible en español en la versión inicial.

---

## Requerimientos Funcionales

### Navegación de Productos:
- Visualización de una lista de productos disponibles.
- Mostrar el stock disponible de cada producto.

### Carrito de Compras:
- Permitir agregar productos al carrito.
- Mostrar un resumen actualizado del carrito con precios, cantidades y total.
- Opción para eliminar productos del carrito o vaciarlo completamente.

### Gestión de Pedidos:
- Confirmar pedidos desde el carrito.
- Actualizar el stock automáticamente al confirmar un pedido.
- Registrar fecha y hora de los pedidos confirmados.

### Gestión de Productos (Administrador):
- Agregar, modificar y eliminar productos del catálogo.
- Editar la cantidad de stock.
- Visualizar claramente los productos sin stock.

---

## Requerimientos No Funcionales

1. **Usabilidad:** Interfaz clara e intuitiva.
2. **Rendimiento:** Operaciones como agregar productos o confirmar pedidos deben procesarse en menos de 3 segundos.
3. **Escalabilidad:** Compatible con futuras integraciones como pasarelas de pago o sistemas de trackeo.
4. **Compatibilidad:** Funcionamiento en navegadores modernos y dispositivos móviles.
5. **Mantenibilidad:** Código modular y documentado para facilitar el mantenimiento y expansión.

---

# Historias de Usuario

## Usuario

### I. Ver productos
Como **usuario**,  
quiero **ver una lista de todos los productos de la tienda**,  
para **elegir los productos que quiero comprar**.

### II. Visualizar carrito
Como **usuario**,  
quiero **tener acceso al carrito**,  
para **tener un control de los productos en los que estoy interesado**.

### III. Visualizar stock
Como **usuario**,  
quiero **visualizar el stock en tiempo real**,  
para **saber la cantidad de unidades disponibles que el sistema posee**.

### IV. Agregar productos al carrito
Como **usuario**,  
quiero **poder agregar productos al carrito**,  
para **tener una lista de los productos que he seleccionado**.

### V. Eliminar productos del carrito
Como **usuario**,  
quiero **poder eliminar un producto especificado**,  
para **regular mi selección antes de finalizar la compra**.

### VI. Sumar productos desde el carrito
Como **usuario**,  
quiero **poder aumentar un producto desde el carrito**,  
para **ajustar las cantidades en base a mis intereses**.

### VII. Restar productos del carrito
Como **usuario**,  
quiero **reducir la cantidad de productos en mi carrito**,  
para **ajustar las cantidades en base a mi presupuesto o necesidades**.

### VIII. Vaciar el carrito
Como **usuario**,  
quiero **poder vaciar el carrito solo con un click**,  
para **borrar todos los productos y así poder empezar de nuevo**.

### IX. Comprar productos
Como **usuario**,  
quiero **poder comprar los productos seleccionados en el carrito**,  
para **finalizar mi compra de manera rápida y segura**.

---

## Administrador

### I. Administrar productos
Como **administrador**,  
quiero **poder gestionar la lista de productos en la tienda**,  
para **mantener actualizada la oferta de productos disponibles para los usuarios**.

### II. Agregar productos a la Base de datos
Como **administrador**,  
quiero **poder añadir nuevos productos a la base de datos**,  
para **ampliar el catálogo y ofrecer más opciones**.

### III. Eliminar productos de la Base de datos
Como **administrador**,  
quiero **poder eliminar productos de la base de datos**,  
para **asegurar que solo los productos disponibles se puedan visualizar**.

### IV. Actualizar los productos
Como **administrador**,  
quiero **actualizar los productos**,  
para **que la cantidad disponible refleje un stock real y evitar así errores en las compras**.

---

## Stack Tecnológico

- **Lenguaje de programación:** Python.
- **Framework de desarrollo web:** Django.
- **Base de datos:** SQLite.
- **Frontend:** HTML5, CSS3.
- **Control de versiones:** Git y GitHub.

---


## Estructura del Proyecto





## Diagrama de Clases
```mermaid
classDiagram
    class Producto {
        -int id
        -String nombre
        -String descripcion
        -float precio
        -int stock
    }

    class Persona {
        -int id
        -String nombre
        -String email
        -String telefono
    }

    class Cliente {
        -String direccion
        +crearCarrito() bool
    }

    class Administrador {
        -String nivel
        +cierreCaja()
    }

    class Carrito {
        -int id
        +existeProducto(producto) bool
        +agregarProducto(producto)
        +guardarCarrito()
        +eliminarProducto(producto)
        +restar(producto)
        +limpiarCarrito()
        +calcular_total() float
        +realizarCompra()
    }

    class MetodoPago {
        <<interface>>
        -int id
        -float monto
    }

    class Efectivo {
        -float monto_recibido
    }

    class BilleteraVirtual {
        -String cuenta
    }

    class Criptomonedas {
        -String wallet
        -String moneda
    }

    class TarjetaCredito {
        -String numeroTarjeta
        -String titular
        -DateTime fechaExpiracion
    }

    class ProcesadorPagos {
        +procesarPago(metodo: MetodoPago) bool
        +generarFactura(cliente: Cliente) Factura
    }

    class Factura {
        -int id
        -Compra compra
        -Cliente cliente
        -DateTime fecha
        -float total
    }

    class User {
        -int id
        -String username
        -String password
        +login(request)
        +logout(request)
    }

    Persona <|-- Cliente
    Persona <|-- Administrador
    Cliente "1" --> "1" Carrito
    Carrito "1" --> "n" Producto
    MetodoPago <|-- Efectivo
    MetodoPago <|-- BilleteraVirtual
    MetodoPago <|-- Criptomonedas
    MetodoPago <|-- TarjetaCredito
    ProcesadorPagos "1" --> "1" MetodoPago
    ProcesadorPagos "1" --> "1" Cliente
    Factura "1" --> "1" Cliente
    User "1" --> "1" Persona
```


---


## Diagrama de Secuencia

```mermaid

```


---


## Pruebas Unitarias
```python
from django.test import TestCase
from .models import Cliente, Producto
from .procesador_pagos import ProcesadorPagos
from .metodos_pago import Efectivo, BilleteraVirtual 

class ProcesadorPagosTestCase(TestCase):

    def setUp(self):
        # Crear productos de prueba
        self.producto1 = Producto.objects.create(nombre='Producto 1', descripcion='Producto de prueba', precio=100.0, stock=10)
        self.producto2 = Producto.objects.create(nombre='Producto 2', descripcion='Otro producto 2', precio=200.0, stock=5)

        # Crear un cliente de prueba
        self.cliente = Cliente.objects.create(user=self.user, direccion='San Martin 500')

    def test_procesar_pago_efectivo(self):
        # Crear un método de pago efectivo
        metodo_pago = Efectivo(monto=300)

        # Procesar el pago
        procesador = ProcesadorPagos()
        resultado = procesador.procesarPago(metodo_pago)

        self.assertTrue(resultado)

    def test_procesar_pago_billetera_virtual(self):
        metodo_pago = BilleteraVirtual(cuenta="12345")

        # Procesar el pago
        procesador = ProcesadorPagos()
        resultado = procesador.procesarPago(metodo_pago)

        self.assertTrue(resultado)

    def test_generar_factura(self):
        # Crear un procesador de pagos
        procesador = ProcesadorPagos()

        self.cliente.carrito.agregarProducto(self.producto1)
        self.cliente.carrito.agregarProducto(self.producto2)

        # Generar factura para el cliente
        factura = procesador.generarFactura(self.cliente)

        self.assertEqual(factura.cliente, self.cliente)
        self.assertEqual(factura.total, 300.0)  
        self.assertIsNotNone(factura.fecha)
```
## Diagrama Entidad-Relación (DER)

```mermaid

```

---


## Diccionario de Datos
