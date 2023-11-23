from django.urls import path
from inicio.views import inicio, paleta, crear_paleta

urlpatterns = [
    path('', inicio, name='inicio'),
    path('paleta/', paleta, name='paleta'),
    path('paleta/crear', crear_paleta, name='crear_paleta')
]