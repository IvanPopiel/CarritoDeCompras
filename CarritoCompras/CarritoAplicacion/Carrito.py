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

    def agregarProducto(self, producto):
        """Este es el método que agrega un producto al carrito"""
        id = str(producto.id)
        if id not in self.carrito.keys():
            self.carrito[id] = {
                "productoId": producto.id,
                "nombre": producto.nombre,
                "descripcion": producto.descripcion,
                "precioFinal": producto.precio,
                "stock": producto.stock,
            }
        else:
            self.carrito[id]["stock"] += 1
            self.carrito[id]["precioFinal"] += producto.precio
        self.guardarCarrito()
        
    def guardarCarrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True

    def eliminarProducto(self, producto):
        id = str(producto.id)
        if id in self.carrito:
            del self.carrito[id]
            self.guardarCarrito()

    def restar(self, producto):
        id = str(producto.id)
        if id in self.carrito.keys():
            self.carrito[id]["stock"] -= 1
            self.carrito[id]["precioFinal"] -= producto.precio
            if self.carrito[id]["stock"] <= 0: self.eliminarProducto(producto)
            self.guardarCarrito()

    def limpiarCarrito(self):
        self.session["carrito"] = {}
        self.session.modified = True
