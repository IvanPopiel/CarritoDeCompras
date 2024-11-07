# Proyecto Carrito de Compras

## JIRA del proyecto
[JIRA del proyecto ![JIRA]([https://upload.wikimedia.org/wikipedia/commons/thumb/c/c7/Jira_logo.svg/512px-Jira_logo.svg.png](https://upload.wikimedia.org/wikipedia/commons/4/4a/Jira_Software%402x-blue.png))](https://ezequiel-grisoski.atlassian.net/jira/software/projects/CAC/boards/3)



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
