from django.db import models
from ckeditor.fields import RichTextField

class Paleta(models.Model):
    marca = models.CharField(max_length=50)
    formato = RichTextField()
    anio = models.IntegerField()

# este def se ve en el catalogo de tablas del panel de administracion /admin
    def __str__(self) -> str:
        return f'{self.marca} - {self.formato} - {self.anio}'