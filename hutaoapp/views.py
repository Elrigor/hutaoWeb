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

    context = {
        "commandsMusica" : commandsMusica,
        "commandsLista" : commandsLista,

        }
    return render(request, template, context)
