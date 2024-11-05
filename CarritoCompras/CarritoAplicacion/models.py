from django.db import models

class Producto(models.Model):
    # crea el id automáticamente
    #atributos que van a tener los productos de la tienda
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    categoria = models.CharField(max_length=40)
    precio = models.FloatField()
    stock = models.IntegerField(default=0) 
    

    def __str__(self):
        return f'{self.nombre} -> {self.precio}'

