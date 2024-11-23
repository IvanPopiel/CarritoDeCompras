class ProcesadorPagos:
    _instancia = None

    def __new__(cls, *args, **kwargs):
        if not cls._instancia:
            cls._instancia = super(ProcesadorPagos, cls).__new__(cls)
        return cls._instancia

    def __init__(self):
        if not hasattr(self, 'inicializado'): 
            self.inicializado = True


    def procesarPago(self, metodo_pago):
        """
        Procesa el pago utilizando un método de pago específico.    
        """
        if isinstance(metodo_pago, MetodoPago):
            print(f"Procesando pago de {metodo_pago.monto} usando {metodo_pago.__class__.__name__}")
            return True
        return False

    def generarFactura(self, cliente):
        # Verifica que el cliente sea válido
        if isinstance(cliente, Cliente):
            # Aquí se podrían agregar más detalles sobre la compra, fecha, total, etc.
            factura = Factura(cliente=cliente, total=cliente.calcular_total(), fecha=datetime.now())
            factura.save()  # Guardar la factura en la base de datos si es necesario
            print(f"Factura generada para el cliente {cliente.nombre} por un total de {factura.total}")
            return factura
        else:
            raise ValueError("El cliente no es válido.")
