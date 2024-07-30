from django.urls import path
from base.views import *

urlpatterns = [
    path('', ventana_index, name='inicio'),
    path('vinilo/', ventana_vinilo, name='vinilo'),
    path('parlante/', ventana_parlante, name='parlante'),
    path('reproductor/', ventana_reproductor, name='reproductor'),
    path('viniloFormulario/', viniloFormulario, name='viniloFormulario'),
    path('parlanteFormulario/', parlanteFormulario, name='parlanteFormulario'),
    path('reproductorFormulario/', reproductorFormulario, name='reproductorFormulario'),
]