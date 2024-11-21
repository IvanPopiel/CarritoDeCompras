# Proyecto Carrito de Compras

## JIRA del proyecto
[JIRA del proyecto](https://ezequiel-grisoski.atlassian.net/jira/software/projects/CAC/boards/3)

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

    class Categoria {
        -int id
        -String nombre
        -String descripcion
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
        cierreCaja()
    }

    class Carrito {
        -int id
        +Cliente cliente
        -List[Producto] productos
        +existeProducto(producto) bool
        +agregarProducto(producto)
        +guardarCarrito()
        +eliminarProducto(producto)
        +restar(producto)
        +limpiarCarrito()
        +calcular_total() float
        realizarCompra()
    }

    class Compra {
        -int id
        -DateTime fecha
        -MetodoPago metodoPago
        -List[Producto] productos
        +realizarFactura()
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

    class Factura {
        -int id
        -Compra compra
        -Cliente cliente
        -DateTime fecha
        -float total
    }

    Categoria "1" --> "n" Producto
    Persona <|-- Cliente
    Persona <|-- Administrador
    Cliente "1" --> "1" Carrito
    Cliente "1" --> "n" Compra
    Carrito "1" --> "n" Producto
    Compra "1" --> "n" Producto
    Compra "1" --> "1" MetodoPago
    MetodoPago <|-- Efectivo
    MetodoPago <|-- BilleteraVirtual
    Factura "1" --> "1" Compra
    Factura "1" --> "1" Cliente
```

## Diagrama de Secuencia

```mermaid
sequenceDiagram
    participant Cliente
    participant Carrito
    participant Producto
    participant MetodoPago
    participant Compra
    participant Factura

    Cliente->>Carrito: Crear Carrito
    Carrito->>Cliente: Carrito creado exitosamente
    Cliente->>Producto: Ver productos disponibles
    Producto->>Cliente: Mostrar productos
    Cliente->>Carrito: Agregar productos al carrito
    Carrito->>Cliente: Producto agregado al carrito
    Cliente->>Carrito: Calcular total
    Carrito->>Cliente: Mostrar total
    Cliente->>MetodoPago: Seleccionar metodo de pago
    MetodoPago->>Cliente: Confirmar metodo de pago
    Cliente->>Compra: Realizar compra
    Compra->>MetodoPago: Procesar pago
    MetodoPago->>Compra: Confirmar pago exitoso
    Compra->>Factura: Generar factura
    Factura->>Cliente: Mostrar factura
    Cliente->>Compra: Finalizar compra
    Compra->>Carrito: Limpiar carrito
```


## Pruebas Unitarias
```python
import unittest
from carrito import Carrito
from producto import Producto
from compra import Compra
from metodo_pago import MetodoPago

class TestCarrito(unittest.TestCase):
    
    def setUp(self):
        # Crear productos de prueba
        self.producto1 = Producto(id=1, nombre="Producto A", descripcion="Descripción A", precio=100.0, stock=10)
        self.producto2 = Producto(id=2, nombre="Producto B", descripcion="Descripción B", precio=200.0, stock=5)
        
        # Crear un carrito de prueba
        self.carrito = Carrito(cliente_id=1)
    
    def test_agregar_producto(self):
        """Probar que agregar un producto al carrito funciona correctamente"""
        self.carrito.agregar_producto(self.producto1)
        self.assertIn(self.producto1, self.carrito.productos)
    
    def test_calcular_total(self):
        """Probar que el cálculo del total del carrito funciona correctamente"""
        self.carrito.agregar_producto(self.producto1)
        self.carrito.agregar_producto(self.producto2)
        total = self.carrito.calcular_total()
        self.assertEqual(total, 300.0)
    
    def test_eliminar_producto(self):
        """Probar que se puede eliminar un producto del carrito"""
        self.carrito.agregar_producto(self.producto1)
        self.carrito.eliminar_producto(self.producto1)
        self.assertNotIn(self.producto1, self.carrito.productos)
    
    def test_realizar_compra(self):
        """Probar que se puede realizar una compra correctamente"""
        self.carrito.agregar_producto(self.producto1)
        metodo_pago = MetodoPago(id=1, monto=100.0)
        compra = Compra(cliente_id=1, metodo_pago=metodo_pago, productos=[self.producto1])
        
        # Simulamos la compra
        resultado_compra = compra.realizar_compra()
        self.assertTrue(resultado_compra)
    
    def test_limpiar_carrito(self):
        """Probar que se puede limpiar el carrito correctamente"""
        self.carrito.agregar_producto(self.producto1)
        self.carrito.limpiar_carrito()
        self.assertEqual(len(self.carrito.productos), 0)

if __name__ == '__main__':
    unittest.main()
```


## Diagrama Entidad-Relación (DER)

```mermaid
erDiagram
    PRODUCTO {
        INT id PK
        VARCHAR(64) nombre
        TEXT descripcion
        FLOAT precio
        INT stock
    }
    
    CATEGORIA {
        INT id PK
        VARCHAR(64) nombre
        TEXT descripcion
    }
    
    PERSONA {
        INT id PK
        VARCHAR(64) nombre
        VARCHAR(64) email
        VARCHAR(15) telefono
    }

    CLIENTE {
        INT persona_id PK, FK
        VARCHAR(128) direccion
    }
    
    ADMINISTRADOR {
        INT persona_id PK, FK
        INT nivel
    }

    CARRITO {
        INT id PK
        INT cliente_id FK
    }

    COMPRA {
        INT id PK
        DATETIME fecha
        INT metodoPago_id FK
        INT cliente_id FK
    }

    METODOPAGO {
        INT id PK
        FLOAT monto
    }

    EFECTIVO {
        INT id PK, FK
        FLOAT monto_recibido
    }

    BILLETERAVIRTUAL {
        INT id PK, FK
        VARCHAR(50) cuenta
    }

    FACTURA {
        INT id PK
        INT compra_id FK
        INT cliente_id FK
        DATETIME fecha
        FLOAT total
    }

    CATEGORIA ||--o{ PRODUCTO : "contiene"
    PERSONA ||--o| CLIENTE : "es"
    PERSONA ||--o| ADMINISTRADOR : "es"
    CLIENTE ||--o| CARRITO : "tiene"
    CLIENTE ||--o{ COMPRA : "realiza"
    CARRITO ||--o{ PRODUCTO : "contiene"
    COMPRA ||--o{ PRODUCTO : "incluye"
    COMPRA ||--o| METODOPAGO : "utiliza"
    METODOPAGO ||--o| EFECTIVO : "es un tipo"
    METODOPAGO ||--o| BILLETERAVIRTUAL : "es un tipo"
    FACTURA ||--o| COMPRA : "corresponde a"
    FACTURA ||--o| CLIENTE : "emitida a"
```

## Diccionario de Datos

### Tabla: `PRODUCTO`
Esta tabla almacena información sobre los productos disponibles en la tienda, incluyendo el nombre, descripción, precio y cantidad en stock.

| Campo        | Tipo de Dato   | Descripción                                                    |
|--------------|----------------|----------------------------------------------------------------|
| `id`         | INT            | Identificador único del producto (clave primaria).             |
| `nombre`     | VARCHAR(64)    | Nombre del producto.                                           |
| `descripcion`| TEXT           | Descripción detallada del producto.                            |
| `precio`     | FLOAT          | Precio del producto.                                           |
| `stock`      | INT            | Cantidad disponible en stock del producto.                     |

---

### Tabla: `CATEGORIA`
Esta tabla almacena las categorías de productos, proporcionando una clasificación para cada producto.

| Campo        | Tipo de Dato   | Descripción                                                    |
|--------------|----------------|----------------------------------------------------------------|
| `id`         | INT            | Identificador único de la categoría (clave primaria).          |
| `nombre`     | VARCHAR(64)    | Nombre de la categoría.                                        |
| `descripcion`| TEXT           | Descripción de la categoría.                                   |

---

### Tabla: `PERSONA`
Esta tabla contiene información básica sobre las personas, incluyendo su nombre, correo electrónico y número de teléfono.

| Campo        | Tipo de Dato   | Descripción                                                    |
|--------------|----------------|----------------------------------------------------------------|
| `id`         | INT            | Identificador único de la persona (clave primaria).            |
| `nombre`     | VARCHAR(64)    | Nombre de la persona.                                          |
| `email`      | VARCHAR(64)    | Correo electrónico de la persona.                              |
| `telefono`   | VARCHAR(15)    | Número de teléfono de la persona.                              |

---

### Tabla: `CLIENTE`
Esta tabla almacena información específica de los clientes, que heredan de la tabla `PERSONA`.

| Campo        | Tipo de Dato   | Descripción                                                    |
|--------------|----------------|----------------------------------------------------------------|
| `persona_id` | INT            | Identificador de la persona (clave primaria y foránea a `PERSONA`). |
| `direccion`  | VARCHAR(128)   | Dirección del cliente.                                         |

---

### Tabla: `ADMINISTRADOR`
Esta tabla almacena información específica de los administradores, que heredan de la tabla `PERSONA`.

| Campo        | Tipo de Dato   | Descripción                                                    |
|--------------|----------------|----------------------------------------------------------------|
| `persona_id` | INT            | Identificador de la persona (clave primaria y foránea a `PERSONA`). |
| `nivel`      | INT            | Nivel del administrador                                             |

---

### Tabla: `CARRITO`
Esta tabla contiene información sobre los carritos de compra de los clientes.

| Campo        | Tipo de Dato   | Descripción                                                    |
|--------------|----------------|----------------------------------------------------------------|
| `id`         | INT            | Identificador único del carrito (clave primaria).              |
| `cliente_id` | INT            | Identificador del cliente (foránea a `CLIENTE`).               |

---

### Tabla: `COMPRA`
Esta tabla almacena los detalles de cada compra realizada por los clientes, incluyendo el método de pago y el cliente asociado.

| Campo         | Tipo de Dato   | Descripción                                                   |
|---------------|----------------|---------------------------------------------------------------|
| `id`          | INT            | Identificador único de la compra (clave primaria).            |
| `fecha`       | DATETIME       | Fecha en que se realizó la compra.                            |
| `metodoPago_id` | INT         | Identificador del método de pago utilizado (foránea a `METODOPAGO`). |
| `cliente_id`  | INT            | Identificador del cliente que realizó la compra (foránea a `CLIENTE`). |

---

### Tabla: `METODOPAGO`
Esta tabla abstracta define la estructura general de un método de pago.

| Campo        | Tipo de Dato   | Descripción                                                    |
|--------------|----------------|----------------------------------------------------------------|
| `id`         | INT            | Identificador único del método de pago (clave primaria).       |
| `monto`      | FLOAT          | Monto pagado.                                                  |

---

### Tabla: `EFECTIVO`
Esta tabla específica almacena información de pagos realizados en efectivo.

| Campo            | Tipo de Dato   | Descripción                                                    |
|------------------|----------------|----------------------------------------------------------------|
| `id`             | INT            | Identificador único (clave primaria y foránea a `METODOPAGO`). |
| `monto_recibido` | FLOAT          | Monto recibido en efectivo.                                    |

---

### Tabla: `BILLETERAVIRTUAL`
Esta tabla específica almacena información de pagos realizados mediante billetera virtual.

| Campo     | Tipo de Dato   | Descripción                                                    |
|-----------|----------------|----------------------------------------------------------------|
| `id`      | INT            | Identificador único (clave primaria y foránea a `METODOPAGO`). |
| `cuenta`  | VARCHAR(50)    | Cuenta de la billetera virtual.                                |

---

### Tabla: `FACTURA`
Esta tabla almacena la información de cada factura generada para las compras.

| Campo        | Tipo de Dato   | Descripción                                                    |
|--------------|----------------|----------------------------------------------------------------|
| `id`         | INT            | Identificador único de la factura (clave primaria).            |
| `compra_id`  | INT            | Identificador de la compra asociada (foránea a `COMPRA`).      |
| `cliente_id` | INT            | Identificador del cliente (foránea a `CLIENTE`).               |
| `fecha`      | DATETIME       | Fecha de emisión de la factura.                                |
| `total`      | FLOAT          | Total de la factura.                                           |

