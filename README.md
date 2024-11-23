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

### I. Registrar una cuenta.
Como **usuario**,  
quiero **poder registrar una cuenta**,  
para **crear un perfil que me permita realizar compras en el sistema**.

### II. Iniciar sesión.
Como **usuario**,  
quiero **poder iniciar sesión**,  
para **acceder a mi cuenta y gestionar mi carrito de compras**.

### III. Recuperar contraseña.
Como **usuario**,  
quiero **poder recuperar mi contraseña en caso de olvido**,  
para **poder acceder sin problemas a mi cuenta**.

### IV. Ver productos.
Como **usuario**,  
quiero **ver una lista de todos los productos de la tienda**,  
para **elegir los productos que quiero comprar**.

### V. Visualizar carrito.
Como **usuario**,  
quiero **tener acceso al carrito**,  
para **tener un control de los productos en los que estoy interesado**.

### VI. Visualizar stock.
Como **usuario**,  
quiero **visualizar el stock en tiempo real**,  
para **saber la cantidad de unidades disponibles que el sistema posee**.

### VII. Agregar productos al carrito.
Como **usuario**,  
quiero **poder agregar productos al carrito**,  
para **tener una lista de los productos que he seleccionado**.

### VIII. Eliminar productos del carrito.
Como **usuario**,  
quiero **poder eliminar un producto especificado**,  
para **regular mi selección antes de finalizar la compra**.

### IX. Sumar productos desde el carrito.
Como **usuario**,  
quiero **poder aumentar un producto desde el carrito**,  
para **ajustar las cantidades en base a mis intereses**.

### X. Restar productos del carrito.
Como **usuario**,  
quiero **reducir la cantidad de productos en mi carrito**,  
para **ajustar las cantidades en base a mi presupuesto o necesidades**.

### XI. Vaciar el carrito.
Como **usuario**,  
quiero **poder vaciar el carrito solo con un click**,  
para **borrar todos los productos y así poder empezar de nuevo**.

### XII. Comprar productos.
Como **usuario**,  
quiero **poder comprar los productos seleccionados en el carrito**,  
para **finalizar mi compra de manera rápida y segura**.

---

## Administrador

### I. Actualizar los productos.
Como **administrador**,  
quiero **poder iniciar sesión en mi cuenta con rol admin**,  
para **gestionar los productos, pedidos y el inventario**.

### II. Ver historial de usuarios.
Como **administrador**,  
quiero **ver un historial de usuarios registrados**,  
para **monitorear las cuentas creadas, y sus respectivas compras**.

### III. Administrar productos.
Como **administrador**,  
quiero **poder gestionar la lista de productos en la tienda**,  
para **mantener actualizada la oferta de productos disponibles para los usuarios**.

### IV. Agregar productos a la Base de datos.
Como **administrador**,  
quiero **poder añadir nuevos productos a la base de datos**,  
para **ampliar el catálogo y ofrecer más opciones**.

### V. Eliminar productos de la Base de datos.
Como **administrador**,  
quiero **poder eliminar productos de la base de datos**,  
para **asegurar que solo los productos disponibles se puedan visualizar**.

### VI. Actualizar los productos.
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

- migrations/
  - Contiene las migraciones generadas por Django para gestionar los cambios en la base de datos.

- static/
  - Contiene archivos estáticos (CSS, imágenes y JavaScript).
  - **css/**: Archivos CSS.
  - **img/**: Imágenes utilizadas en el proyecto.
  - **js/**: Archivos JavaScript.

- templates/
  - Contiene las plantillas HTML que renderiza el servidor.
  - **auth/**
    - **login.html**: Página para iniciar sesión de los usuarios.
    - **register.html**: Página para el registro de nuevos usuarios.
  - **carritoVista.html**: Vista que muestra el contenido del carrito de compras.
  - **checkout.html**: Vista para procesar el pago y finalizar la compra.
  - **index.html**: Página de inicio del sitio web.

- carrito.py
  - Archivos relacionados con la lógica del carrito de compras.

- admin.py
  - Configuración para la administración del sitio web a través del panel de administración de Django.

- apps.py
  - Configuración de la aplicación de Django.

- context_processor.py
  - Contiene funciones para añadir datos al contexto de las vistas (por ejemplo, el carrito de compras en cada vista).

- models.py
  - Define los modelos de la base de datos (por ejemplo, Producto, Cliente, Carrito, etc.).

- tests.py
  - Contiene pruebas unitarias y de integración para garantizar que el sistema funcione correctamente.

- views.py
  - Define las vistas que manejan las solicitudes HTTP y renderizan las plantillas correspondientes.




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

sequenceDiagram
    actor Cliente
    participant Carrito
    participant Producto
    participant ProcesadorPagos
    participant Factura

    Cliente ->> Producto: Seleccionar producto
    Producto ->> Producto: Verificar stock
    Producto -->> Cliente: Confirmar disponibilidad
    Cliente ->> Carrito: Agregar producto al carrito
    Carrito ->> Producto: Validar existencia
    Producto -->> Carrito: Confirmar producto agregado
    Cliente ->> Carrito: Realizar compra
    Carrito ->> ProcesadorPagos: Procesar pago
    ProcesadorPagos -->> Carrito: Confirmar pago exitoso
    Carrito ->> Factura: Solicitar generación de factura
    Factura -->> Cliente: Enviar factura



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
erDiagram
    Producto {
        int idProducto PK
        string nombre
        string descripcion
        float precio
        int stock
    }

    Persona {
        int idPersona PK
        string nombre
        string email
        string telefono
    }

    Cliente {
        int idCliente PK, FK
        string direccion
    }

    Administrador {
        int idAdmin PK, FK
        string nivel
    }

    User {
        int idUser PK
        string username
        string password
        int idPersona FK
    }

    Carrito {
        int idCarrito PK
        int idCliente FK
    }

    Carrito_Producto {
        int idCarrito FK
        int idProducto FK
        int cantidad
    }

    Factura {
        int idFactura PK
        int idCompra FK
        int idCliente FK
        DateTime fecha
        float total
    }

    MetodoPago {
        int idMetodoPago PK
        float monto
    }

    Efectivo {
        int idMetodoPago FK
        float monto_recibido
    }

    BilleteraVirtual {
        int idMetodoPago FK
        string cuenta
    }

    Criptomonedas {
        int idMetodoPago FK
        string wallet
        string moneda
    }

    TarjetaCredito {
        int idMetodoPago FK
        string numeroTarjeta
        string titular
        DateTime fechaExpiracion
    }

    %% Relaciones entre entidades
    Persona ||--o{ Cliente : "es"
    Persona ||--o{ Administrador : "es"
    Persona ||--|| User : "se asocia con"
    Cliente ||--|| Carrito : "tiene"
    Carrito }o--o{ Producto : "contiene"
    Carrito ||--o{ Carrito_Producto : ""
    Producto ||--o{ Carrito_Producto : ""
    Factura ||--|| Cliente : "pertenece a"
    MetodoPago ||--o| Efectivo : "es un"
    MetodoPago ||--o| BilleteraVirtual : "es un"
    MetodoPago ||--o| Criptomonedas : "es un"
    MetodoPago ||--o| TarjetaCredito : "es un"
```

---


## Diccionario de Datos



## Tabla: Producto
| Campo         | Descripción                      | Tipo de Dato  | Tamaño | Restricciones  |
|---------------|----------------------------------|---------------|--------|----------------|
| `idProducto`  | Identificador único del producto | INT           | -      | PK, NOT NULL   |
| `nombre`      | Nombre del producto             | VARCHAR       | 100    | NOT NULL       |
| `descripcion` | Descripción del producto        | TEXT          | -      | NULLABLE       |
| `precio`      | Precio del producto             | FLOAT         | -      | NOT NULL       |
| `stock`       | Cantidad disponible             | INT           | -      | Default: 0     |

---

## Tabla: Persona
| Campo         | Descripción                           | Tipo de Dato  | Tamaño | Restricciones  |
|---------------|---------------------------------------|---------------|--------|----------------|
| `idPersona`   | Identificador único de la persona     | INT           | -      | PK, NOT NULL   |
| `nombre`      | Nombre completo de la persona         | VARCHAR       | 100    | NOT NULL       |
| `email`       | Correo electrónico de la persona      | VARCHAR       | 100    | UNIQUE, NOT NULL |
| `telefono`    | Número de teléfono de la persona      | VARCHAR       | 15     | NULLABLE       |

---

## Tabla: Cliente
| Campo         | Descripción                           | Tipo de Dato  | Tamaño | Restricciones  |
|---------------|---------------------------------------|---------------|--------|----------------|
| `idCliente`   | Identificador único del cliente       | INT           | -      | PK, FK (Persona.idPersona), NOT NULL |
| `direccion`   | Dirección del cliente                | VARCHAR       | 255    | NULLABLE       |

---

## Tabla: Administrador
| Campo         | Descripción                           | Tipo de Dato  | Tamaño | Restricciones  |
|---------------|---------------------------------------|---------------|--------|----------------|
| `idAdmin`     | Identificador único del administrador | INT           | -      | PK, FK (Persona.idPersona), NOT NULL |
| `nivel`       | Nivel del administrador               | VARCHAR       | 50     | NOT NULL       |

---

## Tabla: User
| Campo         | Descripción                           | Tipo de Dato  | Tamaño | Restricciones  |
|---------------|---------------------------------------|---------------|--------|----------------|
| `idUser`      | Identificador único del usuario       | INT           | -      | PK, NOT NULL   |
| `username`    | Nombre de usuario                    | VARCHAR       | 50     | UNIQUE, NOT NULL |
| `password`    | Contraseña del usuario               | VARCHAR       | 255    | NOT NULL       |
| `idPersona`   | Identificador asociado a una persona | INT           | -      | FK (Persona.idPersona), NOT NULL |

---

## Tabla: Carrito
| Campo          | Descripción                                | Tipo de Dato  | Tamaño | Restricciones |
|-----------------|--------------------------------------------|---------------|--------|---------------|
| `idCarrito`     | Identificador único del carrito            | INT           | -      | PK, NOT NULL  |
| `idCliente`     | Identificador del cliente asociado         | INT           | -      | FK (Cliente.idCliente), NOT NULL  |

---

## Tabla: Carrito_Producto
| Campo         | Descripción                                     | Tipo de Dato  | Tamaño | Restricciones |
|---------------|-------------------------------------------------|---------------|--------|---------------|
| `idCarrito`   | Identificador del carrito                       | INT           | -      | FK (Carrito.idCarrito), NOT NULL  |
| `idProducto`  | Identificador del producto                      | INT           | -      | FK (Producto.idProducto), NOT NULL  |
| `cantidad`    | Cantidad del producto en el carrito             | INT           | -      | Default: 1    |

---

## Tabla: Factura
| Campo         | Descripción                          | Tipo de Dato  | Tamaño | Restricciones  |
|---------------|--------------------------------------|---------------|--------|----------------|
| `idFactura`   | Identificador único de la factura    | INT           | -      | PK, NOT NULL   |
| `idCompra`    | Identificador de la compra asociada  | INT           | -      | FK, NOT NULL   |
| `idCliente`   | Identificador del cliente asociado   | INT           | -      | FK, NOT NULL   |
| `fecha`       | Fecha de emisión de la factura       | DATETIME      | -      | NOT NULL       |
| `total`       | Total de la factura                 | FLOAT         | -      | NOT NULL       |

---

## Tabla: MetodoPago
| Campo         | Descripción                          | Tipo de Dato  | Tamaño | Restricciones  |
|---------------|--------------------------------------|---------------|--------|----------------|
| `idMetodoPago`| Identificador único del método pago  | INT           | -      | PK, NOT NULL   |
| `monto`       | Monto del pago                      | FLOAT         | -      | NOT NULL       |

---

### Subtipos de MetodoPago

#### **Efectivo**
| Campo              | Descripción                   | Tipo de Dato  | Tamaño | Restricciones  |
|--------------------|-------------------------------|---------------|--------|----------------|
| `idMetodoPago`     | Identificador del método pago | INT           | -      | FK, NOT NULL   |
| `monto_recibido`   | Monto recibido               | FLOAT         | -      | NOT NULL       |

#### **BilleteraVirtual**
| Campo              | Descripción                   | Tipo de Dato  | Tamaño | Restricciones  |
|--------------------|-------------------------------|---------------|--------|----------------|
| `idMetodoPago`     | Identificador del método pago | INT           | -      | FK, NOT NULL   |
| `cuenta`           | Cuenta de la billetera        | VARCHAR       | 100    | NOT NULL       |

#### **Criptomonedas**
| Campo              | Descripción                   | Tipo de Dato  | Tamaño | Restricciones  |
|--------------------|-------------------------------|---------------|--------|----------------|
| `idMetodoPago`     | Identificador del método pago | INT           | -      | FK, NOT NULL   |
| `wallet`           | Dirección del monedero        | VARCHAR       | 100    | NOT NULL       |
| `moneda`           | Tipo de criptomoneda          | VARCHAR       | 50     | NOT NULL       |

#### **TarjetaCredito**
| Campo              | Descripción                   | Tipo de Dato  | Tamaño | Restricciones  |
|--------------------|-------------------------------|---------------|--------|----------------|
| `idMetodoPago`     | Identificador del método pago | INT           | -      | FK, NOT NULL   |
| `numeroTarjeta`    | Número de la tarjeta          | VARCHAR       | 16     | NOT NULL       |
| `titular`          | Titular de la tarjeta         | VARCHAR       | 100    | NOT NULL       |
| `fechaExpiracion`  | Fecha de expiración           | DATETIME      | -      | NOT NULL       |
