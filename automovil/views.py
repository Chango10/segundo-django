from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from automovil.models import Auto
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class ListadoAutomoviles(ListView):
    model = Auto 
    context_object_name = 'listado_de_automoviles'
    template_name ='automovil/automoviles.html'

    def get_queryset(self):
        marca = self.request.GET.get('marca','')
        if marca:
            listado_de_automoviles = self.model.objects.filter(marca__icontains=marca)
        else:
            listado_de_automoviles = self.model.objects.all()
        return listado_de_automoviles
            

class CrearAutomovil(LoginRequiredMixin,CreateView):
    model = Auto
    template_name = "automovil/crearAutomovil.html"
    fields =['marca','modelo','descripcion','anio']
    success_url = reverse_lazy('automoviles')

class ActualizarAutomovil(LoginRequiredMixin,UpdateView):
    model = Auto
    template_name = "automovil/actualizarAutomovil.html"
    fields =['marca','modelo','descripcion','anio']
    success_url = reverse_lazy('automoviles')

class DetalleAutomovil(DetailView):
    model = Auto
    template_name = "automovil/detalleAutomovil.html"

class EliminarAutomovil(LoginRequiredMixin,DeleteView):
    model = Auto
    template_name = "automovil/eliminarAutomovil.html"
    success_url = reverse_lazy('automoviles')


