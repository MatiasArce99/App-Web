from django.shortcuts import render
from .models import *
from .forms import *
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
        formulario = ViniloFormulario(request.POST)
        print(formulario)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            vinilos = Vinilo(artista=informacion['artista'], album=informacion['album'], genero=informacion['genero'], precio=informacion['precio'])
            vinilos.save()
            return render(request, 'ventanas/inicio.html')
    else:
        formulario = ViniloFormulario()
    return render(request, 'ventanas/viniloFormulario.html', {'formularioVinilo': formulario})

def parlanteFormulario(request):
    if request.method == 'POST':
        parlantes = Parlante(request.POST['marca'], request.POST['tipo'], request.POST['potencia'], request.POST['precio'])
        parlantes.save()
        return render(request, 'ventanas/inicio.html')
    return render(request, 'ventanas/parlanteFormulario.html')

def reproductorFormulario(request):
    if request.method == 'POST':
        reproductor = Reproductor(request.POST['marca'], request.POST['modelo'], request.POST['precio'])
        reproductor.save()
        return render(request, 'ventanas/inicio.html')
    return render(request, 'ventanas/reproductorFormulario.html')