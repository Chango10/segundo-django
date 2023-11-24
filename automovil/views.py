from django.shortcuts import render
from django.views.generic.list import ListView
from automovil.models import Auto

class ListadoAutomoviles(ListView):
    model = Auto 
    context_object_name = 'listado_de_automoviles'
    template_name ='automovil/automoviles.html'
