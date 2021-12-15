from django.shortcuts import render
from .models import Conteudo, Prova, Simulado, Matematica, Redacao

def index(request):
    photo = Conteudo.objects.all()
    texto = Conteudo.objects.all()
    context = {
        'photo': photo,
        'texto': texto,

    }
    return render(request, 'layout.html', context)

def pro(request):
    photo = Prova.objects.all()
    texto = Prova.objects.all()
    context = {
        'photo': photo,
        'texto': texto,

    }
    return render(request, 'prov.html', context)

def cursos(request):
    photo = Conteudo.objects.all()
    texto = Conteudo.objects.all()
    context = {
        'photo': photo,
        'texto': texto,
    }
    return render(request, 'cursoo.html', context)

def conteudos(request):
    photo = Conteudo.objects.all()
    texto = Conteudo.objects.all()
    context = {
        'photo': photo,
        'texto': texto,

    }
    return render(request, 'lista.html', context)


def simul(request):
    photo = Simulado.objects.all()
    texto = Simulado.objects.all()
    context = {
        'photo': photo,
        'texto': texto,

    }
    return render(request, 'simul.html', context)


def Matema(request):
    photo = Matematica.objects.all()
    texto = Matematica.objects.all()
    context = {
        'photo': photo,
        'texto': texto,

    }
    return render(request, 'mate.html', context)


def Redac(request):
    photo = Redacao.objects.all()
    texto = Redacao.objects.all()
    context = {
        'photo': photo,
        'texto': texto,

    }
    return render(request, 'redaca.html', context)


