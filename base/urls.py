from django.urls import path
from base.views import *

urlpatterns = [
    path('', ventana_index, name='inicio'),
    path('vinilo/', ventana_vinilo, name='vinilo'),
    path('parlante/', ventana_parlante, name='parlante'),
    path('reproductor/', ventana_reproductor, name='reproductor'),
]