from django.shortcuts import render
from .models import *
def ventana_index(request):
    return render(request, 'ventanas/inicio.html')
def ventana_vinilo(request):
    vinilos = Vinilo.objects.all()
    contexto = {'vinilo': vinilos}
    return render(request, 'ventanas/vinilo.html', contexto)
def ventana_parlante(request):
    parlantes = Parlante.objects.all()
    contexto = {'parlante': parlantes}
    return render(request, 'ventanas/parlante.html', contexto)
def ventana_reproductor(request):
    reproductor = Reproductor.objects.all()
    contexto = {'rep': reproductor}
    return render(request, 'ventanas/reproductor.html', contexto)

def viniloFormulario(request):
    if request.method == 'POST':
        vinilos = Vinilo(request.POST['artista'], request.POST['album'], request.POST['genero'], request.POST['precio'])
        vinilos.save()
        return render(request, 'ventanas/vinilo.html')
    return render(request, 'ventanas/viniloFormulario.html')

def parlanteFormulario(request):
    return render(request, 'ventanas/parlanteFormulario.html')

def reproductorFormulario(request):
    return render(request, 'ventanas/reproductorFormulario.html')