
from pyexpat import model
from django import views
from django.http import HttpResponse
from django.shortcuts import render, HttpResponse
from django.template import loader
from Apptp.models import *
from Apptp.forms import *

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


# Create your views here.

def inicio(request):
    #avatares = (Avatar.objects.filter(user=request.user.id))

    # , {"url": avatares[0].imagen.url})
    return render(request, "Apptp/inicio.html")


def padre(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    return render(request, "Apptp/padre.html", {"url": avatares[0].imagen.url})


def listbd(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    return render(request, "Apptp/pages.html", {"url": avatares[0].imagen.url})


@login_required
def amigoscoder(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    if request.method == 'POST':

        # aquí mellega toda la información del html
        miFormulario = AmigosCoderForm(request.POST)

        print(miFormulario)

        if miFormulario.is_valid():  # Si pasó la validación de Django

            informacion = miFormulario.cleaned_data
            amigoscoder = AmigosCoder(nombre=informacion['nombre'], apellido=informacion['apellido'],
                                      email=informacion['email'], telefono=informacion['telefono'])

            amigoscoder.save()

            # Vuelvo al inicio o a donde quieran
            return render(request, "Apptp/inicio.html")

    else:

        miFormulario = AmigosCoderForm()  # Formulario vacio para construir el html

    return render(request, "Apptp/amigoscoder.html", {"miFormulario": miFormulario, "url": avatares[0].imagen.url})


@login_required
def amigos(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    if request.method == 'POST':

        # aquí mellega toda la información del html
        miFormulario = AmigosForm(request.POST)

        print(miFormulario)

        if miFormulario.is_valid():  # Si pasó la validación de Django

            informacion = miFormulario.cleaned_data
            persona = Amigos(nombre=informacion['nombre'], apellido=informacion['apellido'],
                             email=informacion['email'], telefono=informacion['telefono'])

            persona.save()

            # Vuelvo al inicio o a donde quieran
            return render(request, "Apptp/inicio.html")

    else:

        miFormulario = AmigosForm()  # Formulario vacio para construir el html

    return render(request, "Apptp/amigos.html", {"miFormulario": miFormulario, "url": avatares[0].imagen.url})


def buscarFamiliar(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    if request.GET["apellido"]:

        apellido = request.GET['apellido']
        familiar = Familiar.objects.filter(apellido__icontains=apellido)

        return render(request, "Apptp/familiar.html", {"familiar": familiar, "apellido": apellido, "url": avatares[0].imagen.url})

    else:
        respuesta = "No enviaste datos"

    return HttpResponse(respuesta)


@login_required
def familiar(request):
    avatares = Avatar.objects.filter(user=request.user.id)

    if request.method == 'POST':

        # aquí mellega toda la información del html
        miFormulario = FamiliarForm(request.POST)

        print(miFormulario)

        if miFormulario.is_valid():  # Si pasó la validación de Django

            informacion = miFormulario.cleaned_data
            persona = Familiar(nombre=informacion['nombre'], apellido=informacion['apellido'],
                               email=informacion['email'], telefono=informacion['telefono'])

            persona.save()

            # Vuelvo al inicio o a donde quieran
            return render(request, "Apptp/familiar.html")

    else:

        miFormulario = FamiliarForm()  # Formulario vacio para construir el html

    return render(request, "Apptp/familiar.html", {"miFormulario": miFormulario, "url": avatares[0].imagen.url})


def leerFamiliar(request):

    familiar = Familiar.objects.all()  # trae todos los familiares

    contexto = {"Familiar": familiar}

    return render(request, "Apptp/leerFamiliar.html", contexto)


def eliminarFamiliar(request, familiar_nombre):

    familiar = Familiar.objects.get(nombre=familiar_nombre)
    familiar.delete()

    # vuelvo al menú
    familiar = Familiar.objects.all()  # trae todos los familiares

    contexto = {"familiar": familiar}

    return render(request, "Apptp/leerfamiliar.html", contexto)


def editarFamiliar(request, familiar_nombre):

    # Recibe el nombre del profesor que vamos a modificar
    familiar = Familiar.objects.get(nombre=familiar_nombre)

    # Si es metodo POST hago lo mismo que el agregar
    if request.method == 'POST':

        # aquí mellega toda la información del html
        miFormulario = FamiliarForm(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:  # Si pasó la validación de Django

            informacion = miFormulario.cleaned_data

            familiar.nombre = informacion['nombre']
            familiar.apellido = informacion['apellido']
            familiar.email = informacion['email']
            familiar.telefono = informacion['telefono']

            familiar.save()

            # Vuelvo al inicio o a donde quieran
            return render(request, "Apptp/familiar.html")
    # En caso que no sea post
    else:
        # Creo el formulario con los datos que voy a modificar
        miFormulario = FamiliarForm(initial={'nombre': familiar.nombre, 'apellido': familiar.apellido,
                                             'email': familiar.email, 'telefono': familiar.telefono})

    # Voy al html que me permite editar
    return render(request, "Apptp/editarfamiliar.html", {"miFormulario": miFormulario, "familiar_nombre": familiar_nombre})


class FamiliarList(LoginRequiredMixin, ListView):

    model = Familiar
    template_name = "Apptp/familiar_list.html"


class FamiliarDetalle(DetailView):

    model = Familiar
    template_name = "Apptp/familiar_detalle.html"


class FamiliarCreacion(CreateView):

    model = Familiar
    success_url = "/Apptp/familiar/list"
    fields = ['nombre', 'apellido', 'email', 'telefono']


class FamiliarUpdate(UpdateView):

    model = Familiar
    success_url = "/Apptp/familiar/list"
    fields = ['nombre', 'apellido', 'email', 'telefono']


class FamiliarDelete(DeleteView):

    model = Familiar
    success_url = "/Apptp/familiar/list"


# Aca comienza el crud de AmigosCoder
def buscarAmigosCoder(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    if request.GET["apellido"]:
        apellido = request.GET['apellido']
        amigoscoder = AmigosCoder.objects.filter(apellido__icontains=apellido)

        return render(request, "Apptp/amigoscoder.html", {"amigoscoder": amigoscoder, "apellido": apellido, "url": avatares[0].imagen.url})

    else:
        respuesta = "No enviaste datos"

    return HttpResponse(respuesta)


def leeramigoscoder(request):
    amigoscoder = AmigosCoder.objects.all()
    contexto = {"amigoscoder": amigoscoder}
    return render(request, "Apptp/leeramigoscoder.html", contexto)


def eliminaramigoscoder(request, amigoscoder_nombre):
    amigoscoder = AmigosCoder.objects.get(nombre=amigoscoder_nombre)
    amigoscoder.delete()

    amigoscoder = AmigosCoder.objects.all()

    contexto = {"amigoscoder": amigoscoder}

    return render(request, "Apptp/leeramigoscoder.html", contexto)


def editaramigoscoder(request, amigoscoder_nombre):
    amigoscoder = AmigosCoder.objects.get(nombre=amigoscoder_nombre)
    if request.method == 'POST':
        miFormulario = AmigosCoderForm(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data

            amigoscoder.nombre = informacion['nombre']
            amigoscoder.apellido = informacion['apellido']
            amigoscoder.email = informacion['email']
            amigoscoder.telefono = informacion['telefono']

            amigoscoder.save()

            return render(request, "Apptp/inicio.html")

    else:
        miFormulario = AmigosCoderForm(initial={
                                       'nombre': amigoscoder.nombre, 'apellido': amigoscoder.apellido, 'email': amigoscoder.email, 'telefono': amigoscoder.telefono})

    return render(request, "Apptp/amigoscoder.html", {"miFormulario": miFormulario, "amigoscoder_nombre": amigoscoder_nombre})

 # Aca sigue con las clases basadas en vista de Amigos coder


class AmigosCoderList(LoginRequiredMixin, ListView):
    model = AmigosCoder
    template_name = "Apptp/amigoscoder_list.html"


class AmigosCoderDetalle(DetailView):
    model = AmigosCoder
    template_name = "Apptp/amigoscoder_detalle.html"


class AmigosCoderCreacion(CreateView):
    model = AmigosCoder
    success_url = "/Apptp/amigoscoder/list"
    fields = ['nombre', 'apellido', 'email', 'telefono']


class AmigosCoderUpdate(UpdateView):
    model = AmigosCoder
    success_url = "/Apptp/amigoscoder/list"
    fields = ['nombre', 'apellido', 'email', 'telefono']


class AmigosCoderDelete(DeleteView):
    model = AmigosCoder
    success_url = "/Apptp/amigoscoder/list"


# joya amigoscoder funciona al 100%


# en la linea 28 esta definido amigos
def buscarAmigos(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    if request.GET["apellido"]:
        apellido = request.GET['apellido']
        amigos = Amigos.objects.filter(apellido__icontains=apellido)

        return render(request, "Apptp/amigos.html", {"amigos": amigos, "apellido": apellido, "url": avatares[0].imagen.url})

    else:
        respuesta = "No enviaste datos"

    return HttpResponse(respuesta)


def leeramigos(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    amigos = Amigos.objects.all()

    contexto = {"amigos": amigos}

    return render(request, "Apptp/leeramigos.html", contexto, {"url": avatares[0].imagen.url})


def eliminaramigos(request, amigos_nombre):
    amigos = Amigos.objects.get(nombre=amigos_nombre)
    amigos.delete()

    amigos = Amigos.objects.all()
    contexto = {"amigos": amigos}
    return render(request, "Apptp/leeramigos.html", contexto)


def editaramigos(request, amigos_nombre):
    amigos = Amigos.objects.get(nombre=amigos_nombre)

    if request.method == 'POST':

        miFormulario = AmigosForm(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            amigos.nombre = informacion['nombre']
            amigos.apellido = informacion['apellido']
            amigos.email = informacion['email']
            amigos.telefono = informacion['telefono']

            amigos.save()

            return render(request, "Apptp/inicio.html")

    else:
        miFormulario = AmigosForm(initial={
                                  'nombre': amigos.nombre, 'apellido': amigos.apellido, 'email': amigos.email, 'telefono': amigos.telefono})

    return render(request, "Apptp/amigos.html", {"miFormulario": miFormulario, "amigos_nombre": amigos_nombre})


class AmigosList(LoginRequiredMixin, ListView):
    model = Amigos
    template_name = "Apptp/amigos_list.html"


class AmigosDetalle(DetailView):
    model = Amigos
    template_name = "Apptp/amigos_detalle.html"


class AmigosCreacion(CreateView):
    model = Amigos
    success_url = "/Apptp/amigos/list"
    fields = ['nombre', 'apellido', 'email', 'telefono']


class AmigosUpdate(UpdateView):
    model = Amigos
    success_url = "/Apptp/amigos/list"
    fields = ['nombre', 'apellido', 'email', 'telefono']


class AmigosDelete(DeleteView):

    model = Amigos
    success_url = "/Apptp/amigos/list"


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contra)

            if user is not None:
                login(request, user)
                return render(request, "Apptp/inicio.html", {"mensaje": f"Bienvenido {usuario}"})
            else:

                return render(request, {"mensaje": "Error, datos incorrectos"})
        else:
            return render(request, "Apptp/inicio.html", {"mesanje": "Error, formulario erroneo"})

    form = AuthenticationForm()

    return render(request, "Apptp/login.html", {'form': form})


def register(request):
    if request.method == 'POST':

        form = UserRegisterform(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request, "Apptp/inicio.html", {"mensaje": "Usuario creado{username} "})
    else:

        form = UserRegisterform()
    return render(request, "Apptp/registro.html", {"form": form})


@login_required
def editarPerfil(request):
    # se instancia el Login;
    usuario = request.user

    if request.method == 'POST':
        miFormulario = UserEditForm(request.POST)
        if miFormulario.is_valid():  # si pasa la validación Django
            informacion = miFormulario.cleaned_data

            # datos que modificaríamos
            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.save()

            return render(request, "Apptp/inicio.html")  # vuelvo a inicio

    else:
        # creo el formulario con los datos que voy a modificar
        miFormulario = UserEditForm(initial={'email': usuario.email})

    # voy al HTML que me permite editar
    return render(request, "Apptp/editarPerfil.html", {"miFormulario": miFormulario, "usuario": usuario})
