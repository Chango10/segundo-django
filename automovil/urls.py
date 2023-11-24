from django.urls import path
from automovil.views import ListadoAutomoviles

urlpatterns = [
    path('automovil/', ListadoAutomoviles.as_view(), name='automoviles'),
]