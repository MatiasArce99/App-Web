from django import forms

class ViniloFormulario(forms.Form):
    artista = forms.CharField(max_length=30)
    album = forms.CharField(max_length=30)
    genero = forms.CharField(max_length=30)
    precio = forms.FloatField()

class ReproductorFormulario(forms.Form):
    marca = forms.CharField(max_length=30)
    modelo = forms.CharField(max_length=30)
    precio = forms.FloatField()

class ParlanteFormulario(forms.Form):
    marca = forms.CharField(max_length=30)
    tipo = forms.CharField(max_length=30)
    potencia = forms.CharField(max_length=30)
    precio = forms.FloatField()