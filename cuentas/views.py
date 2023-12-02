from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as djangoLogin
from cuentas.forms import FormularioRegistro


def login(request):

    if request.method == 'POST':
        formulario = AuthenticationForm(request,data=request.POST)    
        if formulario.is_valid():
            user = formulario.cleaned_data.get('username')
            passw = formulario.cleaned_data.get('password')

            usuario = authenticate(username=user,password=passw)
            djangoLogin(request,usuario)

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