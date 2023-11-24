from django import forms

class BasePaletaFormulario(forms.Form):
    marca = forms.CharField(max_length=20)
    formato = forms.CharField(max_length=250)
    anio = forms.IntegerField()

class CrearPaletaFormulario(BasePaletaFormulario):
    ...

class ActualizarPaletaFormulario(BasePaletaFormulario):
    ...

# v2
class BuscarPaletaFormulario(forms.Form):
    marca = forms.CharField(max_length=30,required=False)
