from django.shortcuts import render
from .models import Commands

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
    commands = Commands.objects.all()
    context = {
        "commands" : commands,
        }
    return render(request, template, context)