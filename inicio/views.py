from django.shortcuts import render, redirect
from inicio.models import Paleta
from inicio.forms import CrearPaletaFormulario
# from django.http import HttpResponse
# from django.template import loader

def inicio(request):
    # v2
    # template = loader.get_template('inicio.html')
    # template_render = template.render({})

    # return HttpResponse(template_render)
    return render(request,'inicio/inicio.html')

def paleta(request):
    marca_a_buscar = request.GET.get('marca')
    if marca_a_buscar:
        listado_paletas = Paleta.objects.filter(marca__icontains=marca_a_buscar)
    else:
        listado_paletas = Paleta.objects.all()

    return render(request,'inicio/paletas.html',{'listado_paletas':listado_paletas})

def crear_paleta(request):
    # V1 HTML
    # print(request.POST.get('marca'))
    # print(request.POST.get('formato'))
    # print(request.POST.get('anio'))
    # if request.method == 'POST':
    #     marca = request.POST.get('marca')
    #     formato = request.POST.get('formato')
    #     anio = request.POST.get('anio')
    #     paleta = Paleta(marca=marca,formato=formato,anio=anio)
    #     paleta.save()

    # v2 django
    # formulario con post, cuando se have click al tobon
    if request.method == 'POST':
        formulario = CrearPaletaFormulario(request.POST)
        if formulario.is_valid():
            info_limpia =formulario.cleaned_data
            marca = info_limpia.get('marca')
            formato = info_limpia.get('formato')
            anio = info_limpia.get('anio')
            paleta = Paleta(marca=marca,formato=formato,anio=anio)
            paleta.save()
            return redirect('paleta')
    # formulario vacio GET, cuando es la primera vez que entra a la pag
    formulario = CrearPaletaFormulario()
    return render(request,'inicio/crear_paleta.html',{'formulario':formulario})
        
