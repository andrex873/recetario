from principal.models import Receta, Comentario
from principal.forms import RecetaForm, ComentarioForm, ContactoForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.mail import EmailMessage

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

def contacto(request):
    if request.method == 'POST':
        formulario = ContactoForm(request.POST)
        if formulario.is_valid():
            titulo = "Mensaje desde la prueba amendez python"
            contenido  = formulario.cleaned_data['mensaje'] + '\n'
            contenido += "Comunicarse a: " + formulario.cleaned_data['correo']
            correo = EmailMessage(titulo,contenido, to=['destinatario_aca@dominio.com'])
            correo.send()
            return HttpResponseRedirect('/')
    else:
        formulario = ContactoForm
    return render_to_response('contactoform.html', {'formulario': formulario}, context_instance = RequestContext(request))

def nueva_receta(request):
    if request.method == 'POST':
        formulario = RecetaForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/recetas')
    else:
        formulario = RecetaForm()
    return render_to_response('recetaform.html', {'formulario': formulario}, context_instance = RequestContext(request))        

def nuevo_comentario(request):
    if request.method == 'POST':
        formulario = ComentarioForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/recetas')
    else:
        formulario = ComentarioForm()
    return render_to_response('comentarioform.html', {'formulario': formulario}, context_instance = RequestContext(request))