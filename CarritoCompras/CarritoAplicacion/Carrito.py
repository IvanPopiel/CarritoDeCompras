#aca va toda la logica, agregarProducto al carrito
#guardarCarrito guardar lo seleccionado en el carrito
#eliminarProducto eliminar un producto del carrito
#restar resta una unidad del producto seleccionado
#limpiarCarrito vacia el carrito entero
#se uso session para poder tener persistencia.

class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            self.session["carrito"] = {}
            self.carrito = self.session["carrito"]
        else:
            self.carrito = carrito

    def existeProducto(self, producto):
        """Verifica si un producto está en el carrito"""
        id = str(producto.id)
        return id in self.carrito

    def agregarProducto(self, producto):
        """Este es el método que agrega un producto al carrito"""
        id = str(producto.id)
        
        # Verificar si el producto ya está en el carrito
        if id not in self.carrito:
            # Si no está en el carrito, agregamos el producto con el stock original
            self.carrito[id] = {
                "productoId": producto.id,
                "nombre": producto.nombre,
                "descripcion": producto.descripcion,
                "precioFinal": producto.precio,
                "stock": 1,  # La cantidad en el carrito, por ahora es 1
                "stockOriginal": producto.stock,  # Guardamos el stock original del producto
            }
        else:
            # Si ya está en el carrito, solo aumentamos la cantidad y el precio final
            self.carrito[id]["stock"] += 1
            self.carrito[id]["precioFinal"] += producto.precio

        # Guardamos el carrito actualizado en la sesión
        self.guardarCarrito()

    def guardarCarrito(self):
        """Guarda el carrito en la sesión"""
        self.session["carrito"] = self.carrito
        self.session.modified = True

    def eliminarProducto(self, producto):
        """Elimina un producto del carrito"""
        id = str(producto.id)
        if id in self.carrito:
            del self.carrito[id]
            self.guardarCarrito()

    def restar(self, producto):
        """Resta una unidad del producto en el carrito"""
        id = str(producto.id)
        if id in self.carrito.keys():
            self.carrito[id]["stock"] -= 1
            self.carrito[id]["precioFinal"] -= producto.precio
            if self.carrito[id]["stock"] <= 0:
                self.eliminarProducto(producto)
            self.guardarCarrito()

    def limpiarCarrito(self):
        """Limpia el carrito y restaura el stock original de los productos"""
        self.session["carrito"] = {}
        self.session.modified = True


    def calcular_total(self):
        """Calcula el total del carrito sumando los precios finales de los productos."""
        total = 0
        for item in self.carrito.values():
            total += float(item["precioFinal"])
        return total