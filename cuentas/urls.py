from django.urls import path
from cuentas.views import login, registro, editar_usuario, CambiarPassword
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', login, name='login'),
    path('registro/', registro, name='registrarse'),
    path('logout/', LogoutView.as_view(template_name='cuentas/logout.html'), name='logout'),
    path('perfil/editar/', editar_usuario, name='editar_usuario'),
    path('perfil/editar/password', CambiarPassword.as_view(), name='cambiar_password'),
]