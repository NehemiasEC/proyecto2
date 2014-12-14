from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from datetime import datetime
from app.models import *
from django.shortcuts import render_to_response, get_object_or_404

# Create your views here.

def home(request):
    usuario="hola usuario anonimo porque no tengo base de datos aun"
    return render_to_response('index.html',locals())

def estrategia(resquest):
    return render_to_response('estrategia.html',locals())

def blog(request):
    categorias=Categoria.objects.all()
    enlaces = Enlace.objects.filter(categoria = categorias)
    template = "blog.html"
    return render_to_response(template,locals())

def desarrollo(request):
    return render_to_response('desarrollo.html',locals())

def categoria(request,id_categoria):
    categorias=Categoria.objects.all()
    cat=Categoria.objects.get(pk=id_categoria)
    enlaces=Enlace.objects.filter(categoria=cat)
    templates="blog.html"
    return render_to_response(templates,locals())