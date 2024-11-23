from django.db import models
from django.contrib.auth.models import User
class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    categoria = models.CharField(max_length=40)
    precio = models.FloatField()
    stock = models.IntegerField(default=0) 
    

    def __str__(self):
        return f'{self.nombre} -> {self.precio}'

class Persona(models.Model):
    """
    Clase base para representar a una persona con datos comunes.
    Está asociada a un usuario de Django.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="persona")
    telefono = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.user.get_full_name()


class Cliente(Persona):
    """
    Cliente que hereda de Persona y tiene funcionalidades específicas.
    """
    direccion = models.CharField(max_length=255, blank=True, null=True)


class Administrador(Persona):
    """
    Administrador que hereda de Persona y tiene funciones administrativas.
    """
    nivel = models.CharField(max_length=50, blank=True, null=True)

    def cierreCaja(self):
        return "Cierre de caja realizado"