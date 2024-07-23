from django.shortcuts import render

def ventana_index(request):
    return render(request, 'ventanas/inicio.html')
def ventana_vinilo(request):
    return render(request, 'ventanas/vinilo.html')
def ventana_parlante(request):
    return render(request, 'ventanas/parlante.html')
def ventana_reproductor(request):
    return render(request, 'ventanas/reproductor.html')