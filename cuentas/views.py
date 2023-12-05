from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as djangoLogin
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from cuentas.forms import FormularioRegistro, FormularioEditarUsuario
from cuentas.models import DatosExtras


def login(request):

    if request.method == 'POST':
        formulario = AuthenticationForm(request,data=request.POST)    
        if formulario.is_valid():
            user = formulario.cleaned_data.get('username')
            passw = formulario.cleaned_data.get('password')

            usuario = authenticate(username=user,password=passw)
            djangoLogin(request,usuario)

            DatosExtras.objects.get_or_create(user=request.user) #aca me traigo los datos de bio del usuario logueado
            return redirect('inicio')
     
    formulario = AuthenticationForm()
    return render(request,'cuentas/login.html',{'formulario_login':formulario})


def registro(request):
    formulario =FormularioRegistro()
    
    if request.method =='POST':
        formulario = FormularioRegistro(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('login')

    return render(request,'cuentas/registro.html',{'formulario_registro':formulario})

def editar_usuario(request):
    # el initial es para inicializar variables de modelos que no estan en el User en este caso, 
    # trae lo de datos extra
    formulario =FormularioEditarUsuario(initial={'biografia':request.user.datosextras.biografia,'avatar':request.user.datosextras.avatar},instance=request.user)   

    if request.method =='POST':
        formulario =FormularioEditarUsuario(request.POST, request.FILES, instance=request.user)   
        
        if formulario.is_valid():
            nueva_biografia = formulario.cleaned_data.get('biografia') # acá obtengo los datos de la tabla relacionada para guardar luego
            nuevo_avatar = formulario.cleaned_data.get('avatar') 

            if nueva_biografia:
                request.user.datosextras.biografia = nueva_biografia  #datosextras es el nombre de la clase, pero todo en minusculas
            if nuevo_avatar:
                request.user.datosextras.avatar = nuevo_avatar  #datosextras es el nombre de la clase, pero todo en minusculas

            request.user.datosextras.save()
            formulario.save()   #aca se guarda el modelo de datos User, no así los de tablas relacionadas

            return redirect('editar_usuario') #para la entrega final se requiere ir directamente al perfil
        
    return render(request,'cuentas/editar_usuario.html',{'formulario':formulario})

class CambiarPassword(PasswordChangeView):
    template_name = 'cuentas/cambiar_pass.html'
    success_url = reverse_lazy('editar_usuario')
