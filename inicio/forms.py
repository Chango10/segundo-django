from django import forms

class CrearPaletaFormulario(forms.Form):
    marca = forms.CharField(max_length=20)
    formato = forms.CharField(max_length=250)
    anio = forms.IntegerField()