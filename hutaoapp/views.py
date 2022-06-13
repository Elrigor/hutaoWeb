from unicodedata import name
from django.shortcuts import render
from .models import Command

def index(request):    
    template = 'hutaoapp/index.html'
    context = {}
    return render(request, template, context)

def notfound(request):    
    template = 'hutaoapp/notfound.html'
    context = {}
    return render(request, template, context)

def commands(request):    
    template = 'hutaoapp/commands.html'
    commandsMusica = Command.objects.all().filter(categoria__name="Musica")
    commandsLista = Command.objects.all().filter(categoria__name="Lista")
    commandsAnimales = Command.objects.all().filter(categoria__name="Animales")
    commandsGenshin = Command.objects.all().filter(categoria__name="Genshin")
    commandsPerfil = Command.objects.all().filter(categoria__name="Perfil")
    commandsMoneda = Command.objects.all().filter(categoria__name="Moneda")
    commandsDivertidos = Command.objects.all().filter(categoria__name="Divertidos")
    commandsUtiles = Command.objects.all().filter(categoria__name="Utiles")
    
    context = {
        "commandsMusica" : commandsMusica,
        "commandsLista" : commandsLista,
        "commandsAnimales" : commandsAnimales,
        "commandsGenshin" : commandsGenshin,
        "commandsPerfil" : commandsPerfil,
        "commandsMoneda" : commandsMoneda,
        "commandsDivertidos" : commandsDivertidos,
        "commandsUtiles" : commandsUtiles,
        }

    return render(request, template, context)
