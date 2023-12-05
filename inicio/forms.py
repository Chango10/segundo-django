from django import forms
from ckeditor.fields import RichTextFormField

class BasePaletaFormulario(forms.Form):
    marca = forms.CharField(max_length=20)
    formato = RichTextFormField()
    anio = forms.IntegerField()

class CrearPaletaFormulario(BasePaletaFormulario):
    ...

class ActualizarPaletaFormulario(BasePaletaFormulario):
    ...

# v2
class BuscarPaletaFormulario(forms.Form):
    marca = forms.CharField(max_length=30,required=False)
