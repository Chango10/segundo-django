from django.db import models

class Auto(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=250)
    anio = models.DateField()

# este def se ve en el catalogo de tablas del panel de administracion /admin
    def __str__(self) -> str:
        return f'{self.marca} - {self.modelo} - {self.anio}'