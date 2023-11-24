from django.urls import path
from inicio.views import inicio, paleta, crear_paleta, eliminarPaleta, actualizarPaleta, detallePaleta

urlpatterns = [
    path('', inicio, name='inicio'),
    path('paleta/', paleta, name='paleta'),
    path('paleta/crear', crear_paleta, name='crear_paleta'),
    path('paleta/<int:paleta_id>/eliminar/', eliminarPaleta, name='eliminarPaleta'),
    path('paleta/<int:paleta_id>/actualizar/', actualizarPaleta, name='actualizarPaleta'),
    path('paleta/<int:paleta_id>', detallePaleta, name='detallePaleta'),
]