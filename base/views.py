from django.shortcuts import render
from .models import Vinilo
def ventana_index(request):
    return render(request, 'ventanas/inicio.html')
def ventana_vinilo(request):
    vinilos = Vinilo.objects.all()
    return render(request, 'ventanas/vinilo.html', {'vinilos': vinilos})
def ventana_parlante(request):
    return render(request, 'ventanas/parlante.html')
def ventana_reproductor(request):
    return render(request, 'ventanas/reproductor.html')