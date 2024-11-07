# Proyecto Carrito de Compras

## JIRA del proyecto
[JIRA del proyecto](https://ezequiel-grisoski.atlassian.net/jira/software/projects/CAC/boards/3)

## Diagrama de Clases
```mermaid
classDiagram
    class Usuario {
        -int id
        -String nombre
        -String email
        -String direccion
        -String telefono
        -Carrito carrito
        -List[Factura] facturas
        +crearFactura()
    }

    class Carrito {
        -int id
        -List[ItemCarrito] items
        +agregarProducto(producto: Producto)
        +eliminarProducto(producto: Producto)
        +restar(producto: Producto) 
        +limpiarCarrito()
    }

    class Producto {
        -int id
        -String nombre
        -String descripcion
        -String categoria
        -float precio
        -int stock
    }

    class Factura {
        -int id
        -Usuario usuario
        -DateTime fecha
        -List[Producto] productos
        -float total
    }

    Usuario "1" --> "1" Carrito 
    Usuario "1" --> "n" Factura 
    Carrito "1" --> "n" Producto 
    Factura "1" --> "n" Producto 
```


## Diagrama Entidad-Relación (DER)

```mermaid
erDiagram
    PRODUCTO {
        int id
        VARCHAR(50) nombre
        TEXT descripcion
        VARCHAR(40) categoria
        FLOAT precio
        int stock
    }
```

## Diccionario de Datos

### Tabla: `PRODUCTO`

Esta tabla almacena información sobre los productos disponibles en la tienda, incluyendo el nombre, descripción, categoría, precio y stock.

| Campo        | Tipo de Dato   | Descripción                                                    |
|--------------|----------------|----------------------------------------------------------------|
| `id`         | int            | Identificador único del producto (clave primaria).             |
| `nombre`     | VARCHAR(50)     | Nombre del producto.                                           |
| `descripcion`| TEXT           | Descripción detallada del producto.                            |
| `categoria`  | VARCHAR(40)     | Categoría a la que pertenece el producto.                      |
| `precio`     | FLOAT          | Precio del producto.                                           |
| `stock`      | int            | Cantidad disponible en stock del producto.                     |
