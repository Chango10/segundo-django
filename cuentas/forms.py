from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class FormularioRegistro(UserCreationForm):
        email = forms.EmailField()
        password1 = forms.CharField(label='Contraseña',widget=forms.PasswordInput)
        password2 = forms.CharField(label='Confirmar Contraseña',widget=forms.PasswordInput)

        class Meta:
                model=User
                fields =['username','email','password1', 'password2']
                help_text = {key:'' for key in fields}


class FormularioEditarUsuario(UserChangeForm):
        password=None
        email = forms.EmailField(widget=forms.EmailInput)
        first_name = forms.CharField(label='Cambiar Nombre', max_length=20, required=False)
        last_name = forms.CharField(label='Cambiar Apellido', max_length=20, required=False)
        biografia = forms.CharField( max_length=100, required=False,widget=forms.Textarea)
        avatar = forms.ImageField(required=False)

        class Meta:
                model=User
                fields =['email','first_name', 'last_name','biografia','avatar']
