from django.urls import path
from base.views import ventana_index, ventana_vinilo, ventana_parlante, ventana_reproductor

urlpatterns = [
    path('', ventana_index),
    path('vinilo/', ventana_vinilo),
    path('parlante/', ventana_parlante),
    path('reproductor/', ventana_reproductor),
]