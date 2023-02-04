from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from AppProyecto.models import Tazas, Funkos, Remeras
from AppProyecto.forms import TazasFormulario, FunkosFormulario, RemerasFormulario, UserRegisterForm, UserEditForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Create your views here.
@login_required
def listar_tazas(request):
    contexto = {
        'tazas': Tazas.objects.all()
    }
    return render(
        request=request,
        template_name='AppProyecto/listar_tazas.html',
        context=contexto,
    )

@login_required
def listar_funkos(request):
    contexto = {
        'funkos': Funkos.objects.all()
    }
    return render(
        request=request,
        template_name='AppProyecto/listar_funkos.html',
        context=contexto,
    )

@login_required
def listar_remeras(request):
    contexto = {
        'remeras': Remeras.objects.all()
    }
    return render(
        request=request,
        template_name='AppProyecto/listar_remeras.html',
        context=contexto,
    )

def sobre_mi(request):
      return render(request, "AppProyecto/sobre_mi.html")

def crear_taza(request):
      if request.method == 'POST':

            miFormulario = TazasFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data

                  taza = Tazas(categoria=informacion['categoria'], nombre=informacion['nombre'],
                  precio=informacion['precio'], informacion=informacion['informacion'], colores=informacion['colores'], 
                  imagenTaza=informacion['imagenTaza']) 

                  taza.save()

                  return render(request, "AppProyecto/inicio.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario= TazasFormulario() #Formulario vacio para construir el html

      return render(request, "AppProyecto/crear_tazas.html", {"miFormulario":miFormulario})

def crear_funko(request):
      if request.method == 'POST':

            miFormulario = FunkosFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data

                  funko = Funkos(categoria=informacion['categoria'], nombre=informacion['nombre'],
                  precio=informacion['precio'], informacion=informacion['informacion'], 
                  imagenFunko=informacion['imagenFunko']) 

                  funko.save()

                  return render(request, "AppProyecto/inicio.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario= FunkosFormulario() #Formulario vacio para construir el html

      return render(request, "AppProyecto/crear_funkos.html", {"miFormulario":miFormulario})

def crear_remera(request):
      if request.method == 'POST':

            miFormulario = RemerasFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data

                  remera = Remeras(categoria=informacion['categoria'], nombre=informacion['nombre'],
                  precio=informacion['precio'], talle=informacion['talle'], 
                  imagenRemera=informacion['imagenRemera']) 

                  remera.save()

                  return render(request, "AppProyecto/inicio.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario= RemerasFormulario() #Formulario vacio para construir el html

      return render(request, "AppProyecto/crear_remeras.html", {"miFormulario":miFormulario})

def editar_taza(request, taza_nombre):
    # Recibe el nombre del profesor que vamos a modificar
    taza = Tazas.objects.get(nombre=taza_nombre)
    # Si es metodo POST hago lo mismo que el agregar
    if request.method == 'POST':
        # aquí mellega toda la información del html
        miFormulario = TazasFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:  # Si pasó la validación de Django

            informacion = miFormulario.cleaned_data

            taza.categoria = informacion['categoria']
            taza.nombre = informacion['nombre']
            taza.precio = informacion['precio']
            taza.informacion = informacion['informacion']
            taza.colores = informacion['colores']
            taza.imagenTaza = informacion['imagenTaza']

            taza.save()

            # Vuelvo al inicio o a donde quieran
            taza = Tazas.objects.all() #trae todos las mallas
            contexto= {"taza":taza} 
            return render(request, "AppProyecto/listar_tazas.html",contexto)
           
    # En caso que no sea post
    else:
        # Creo el formulario con los datos que voy a modificar
        miFormulario = TazasFormulario(initial={'categoria': taza.categoria,'nombre': taza.nombre, 'precio': taza.precio,
                                                   'informacion': taza.informacion, 'colores': taza.colores, 'imagenTaza': taza.imagenTaza})

    # Voy al html que me permite editar
    return render(request, "AppProyecto/editar_tazas.html", {"miFormulario": miFormulario, "taza_nombre": taza_nombre})


def editar_funko(request, funko_nombre):
    # Recibe el nombre del profesor que vamos a modificar
    funko = Funkos.objects.get(nombre=funko_nombre)
    # Si es metodo POST hago lo mismo que el agregar
    if request.method == 'POST':
        # aquí mellega toda la información del html
        miFormulario = TazasFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:  # Si pasó la validación de Django

            informacion = miFormulario.cleaned_data

            funko.categoria = informacion['categoria']
            funko.nombre = informacion['nombre']
            funko.precio = informacion['precio']
            funko.informacion = informacion['informacion']
            funko.imagenFunko = informacion['imagenFunko']

            funko.save()

            # Vuelvo al inicio o a donde quieran
            funko = Funkos.objects.all() #trae todos las mallas
            contexto= {"funko":funko} 
            return render(request, "AppProyecto/listar_funkos.html",contexto)
           
    # En caso que no sea post
    else:
        # Creo el formulario con los datos que voy a modificar
        miFormulario = FunkosFormulario(initial={'categoria': funko.categoria,'nombre': funko.nombre, 'precio': funko.precio,
                                                   'informacion': funko.informacion, 'imagenFunko': funko.imagenFunko})

    # Voy al html que me permite editar
    return render(request, "AppProyecto/editar_funkos.html", {"miFormulario": miFormulario, "funko_nombre": funko_nombre})

def editar_remera(request, remera_nombre):
    # Recibe el nombre del profesor que vamos a modificar
    remera = Remeras.objects.get(nombre=remera_nombre)
    # Si es metodo POST hago lo mismo que el agregar
    if request.method == 'POST':
        # aquí mellega toda la información del html
        miFormulario = RemerasFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:  # Si pasó la validación de Django

            informacion = miFormulario.cleaned_data

            remera.categoria = informacion['categoria']
            remera.nombre = informacion['nombre']
            remera.precio = informacion['precio']
            remera.talle = informacion['talle']
            remera.imagenRemera = informacion['imagenRemera']

            remera.save()

            # Vuelvo al inicio o a donde quieran
            remera = Remeras.objects.all() #trae todos las mallas
            contexto= {"remera":remera} 
            return render(request, "AppProyecto/listar_remeras.html",contexto)
           
    # En caso que no sea post
    else:
        # Creo el formulario con los datos que voy a modificar
        miFormulario = RemerasFormulario(initial={'categoria': remera.categoria,'nombre': remera.nombre, 'precio': remera.precio,
                                                   'talle': remera.talle, 'imagenRemera': remera.imagenRemera})

    # Voy al html que me permite editar
    return render(request, "AppProyecto/editar_remeras.html", {"miFormulario": miFormulario, "remera_nombre": remera_nombre})

def eliminar_taza(request, taza_nombre):
      taza = Tazas.objects.get(nombre=taza_nombre)
      taza.delete()
      # vuelvo al menú
      taza = Tazas.objects.all() #trae toda la ropa interior
      contexto = {"taza":taza}
      return render(request, "AppProyecto/listar_tazas.html",contexto)

def eliminar_funko(request, funko_nombre):
      funko = Funkos.objects.get(nombre=funko_nombre)
      funko.delete()
      # vuelvo al menú
      funko = Funkos.objects.all() #trae toda la ropa interior
      contexto = {"funko":funko}
      return render(request, "AppProyecto/listar_funkos.html",contexto)

def eliminar_remera(request, remera_nombre):
      remera = Remeras.objects.get(nombre=remera_nombre)
      remera.delete()
      # vuelvo al menú
      remera = Remeras.objects.all() #trae toda la ropa interior
      contexto = {"remera":remera}
      return render(request, "AppProyecto/listar_remeras.html",contexto)

def taza_detalle(request, taza_id):
    taza = Tazas.objects.get(id=taza_id)
    contexto = {
        'taza': taza
    }
    return render(
        request=request,
        template_name='AppProyecto/detalle_taza.html',
        context=contexto,
    )

def funko_detalle(request, funko_id):
    funko = Funkos.objects.get(id=funko_id)
    contexto = {
        'funko': funko
    }
    return render(
        request=request,
        template_name='AppProyecto/detalle_funko.html',
        context=contexto,
    )

def remera_detalle(request, remera_id):
    remera = Remeras.objects.get(id=remera_id)
    contexto = {
        'remera': remera
    }
    return render(
        request=request,
        template_name='AppProyecto/detalle_remera.html',
        context=contexto,
    )

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():  # Si pasó la validación de Django

            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username= usuario, password=contrasenia)

            if user is not None:
                login(request, user)

                return render(request, "AppProyecto/inicio.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request, "AppProyecto/inicio.html", {"mensaje":"Datos incorrectos"})
           
        else:

            return render(request, "AppProyecto/inicio.html", {"mensaje":"Formulario erroneo"})

    form = AuthenticationForm()

    return render(request, "AppProyecto/login.html", {"form": form})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request,"AppProyecto/inicio.html" ,  {"mensaje":"Usuario Creado :)"})
    else:      
        form = UserRegisterForm()     

    return render(request,"AppProyecto/registro.html" ,  {"form":form})


@login_required
def inicio(request):
      return render(request, "AppProyecto/inicio.html")

@login_required
def editar_perfil(request):

    usuario = request.user

    if request.method == 'POST':

        miFormulario = UserEditForm(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            usuario.email = informacion['username']
            usuario.password1 = informacion['contrasenia']
            usuario.password2 = informacion['repetircontrasenia']
            usuario.first_name = informacion['first_name']
            usuario.last_name = informacion['last_name']

            usuario.save()

            return render(request, "AppProyecto/inicio.html")

    else:

        miFormulario = UserEditForm(initial={'email': usuario.email})

    return render(request, "AppProyecto/editar_perfil.html", {"miFormulario": miFormulario, "usuario": usuario})

@login_required
def buscar_tazas(request):
    if request.GET["nombre"]:
        nombre = request.GET['nombre']
        taza = Tazas.objects.filter(nombre__contains=nombre)
      
        return render(request, "AppProyecto/busqueda_tazas.html", {"taza":taza, "nombre": nombre})
    else:
        respuesta = "No enviaste datos"
        return HttpResponse(respuesta)

@login_required
def buscar_funkos(request):
    if request.GET["nombre"]:
        nombre = request.GET['nombre']
        funko = Funkos.objects.filter(nombre__contains=nombre)
    
        return render(request, "AppProyecto/busqueda_funkos.html", {"funko":funko, "nombre": nombre})
    else:
        respuesta = "No enviaste datos"
        return HttpResponse(respuesta)

@login_required
def buscar_remeras(request):
    if request.GET["nombre"]:
        nombre = request.GET['nombre']
        remera = Remeras.objects.filter(nombre__contains=nombre)
        return render(request, "AppProyecto/busqueda_remeras.html", {"remera":remera, "nombre": nombre})
    else:
        respuesta = "No enviaste datos"
        return HttpResponse(respuesta)