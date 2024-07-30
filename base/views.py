from django.http import HttpResponse
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
        formulario = ParlanteFormulario(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            parlantes = Parlante(marca=informacion['marca'], tipo=informacion['tipo'], potencia=informacion['potencia'], precio=informacion['precio'])
            parlantes.save()
            return render(request, 'ventanas/inicio.html')
    else:
        formulario = ParlanteFormulario()
    return render(request, 'ventanas/parlanteFormulario.html', {'formularioParlante': formulario})

def reproductorFormulario(request):
    if request.method == 'POST':
        formulario = ReproductorFormulario(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            reproductor = Reproductor(marca=informacion['marca'], modelo=informacion['modelo'], precio=informacion['precio'])
            reproductor.save()
            return render(request, 'ventanas/inicio.html')
    else:
        formulario = ReproductorFormulario()
    return render(request, 'ventanas/reproductorFormulario.html', {'formularioReproductor': formulario})

def busquedaVinilo(request):
    return render(request, 'ventanas/busquedaVinilo.html')

def buscar(request):
    if request.GET['artista']:
        artista = request.GET['artista']
        vinilos = Vinilo.objects.filter(artista__icontains=artista)
        return render(request, 'ventanas/resultadoBusqueda.html', {'vinilos': vinilos})
    else:
        respuesta = 'Vinilo no disponible'
    return HttpResponse(respuesta)