from django.urls import path
from automovil.views import ListadoAutomoviles, CrearAutomovil, DetalleAutomovil, ActualizarAutomovil, EliminarAutomovil

urlpatterns = [
    path('automovil/', ListadoAutomoviles.as_view(), name='automoviles'),
    path('automovil/crear/', CrearAutomovil.as_view(), name='crear_Automovil'),
    path('automovil/<int:pk>/', DetalleAutomovil.as_view(), name='detalle_Automovil'),
    path('automovil/<int:pk>/actualizar/', ActualizarAutomovil.as_view(), name='actualizar_Automovil'),
    path('automovil/<int:pk>/eliminar/', EliminarAutomovil.as_view(), name='eliminar_Automovil'),
]