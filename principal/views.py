from principal.models import Receta, Comentario
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

def sobre(request):
    html = "<html><body><h2>Esta es la vista 'sobre'</h2></body></html>"
    return HttpResponse(html)

def inicio(request):
    recetas = Receta.objects.all()
    return render_to_response('inicio.html', {'listaRecetas': recetas})

def usuarios(request):
    usuarios = User.objects.all()
    recetas = Receta.objects.all()
    return render_to_response('usuarios.html', {'listaUsuarios': usuarios, 'ListaRecetas': recetas})

def lista_recetas(request):
    recetas = Receta.objects.all()
    return render_to_response('lista_recetas.html', {'listaRecetas': recetas}, context_instance=RequestContext(request))

def detalle_receta(request, id_receta):
    dato = get_object_or_404(Receta, pk=id_receta)
    comentarios = Comentario.objects.filter(receta=dato)
    return render_to_response('detalle_receta.html', {'receta': dato, 'listaComentarios': comentarios}, context_instance=RequestContext(request))