from django.shortcuts import redirect, render
from django.views.generic import UpdateView, DeleteView, DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin

from AppCoder.forms import FutbolistasFormulario, BasquetbolistasFormulario, RegistroUsuarioForm, TenistasFormulario, LoginAuthenticationForm, EditarUsuarioForm, AvatarForm
from .models import Futbolista, Basquetbolista, Tenista, Avatar

# Create your views here.

def index(request):
    return render(request, 'AppCoder/index.html', {})

def lista_futbolistas(request):
    futbolistas = None
    error = None
    if request.method =='GET':
        nombre = request.GET.get('nombre', '')
        apellido = request.GET.get('apellido','')
        edad = request.GET.get('edad',None)
        if nombre == '' and apellido == '' and edad == '' : #Se considera que si no introdujo ningún campo, está queriendo ver todos.
            futbolistas = Futbolista.objects.all()
        elif nombre: 
            if nombre.replace(' ','').isalpha(): #Por si se introduce más de un nombre
                futbolistas = Futbolista.objects.filter(nombre = nombre)
            else:
                error = 'Debe ingresar un nombre válido'
        
        elif apellido:
            if apellido.replace(' ','').isalpha(): #Por si se introduce más de un nombre
                futbolistas = Futbolista.objects.filter(apellido = apellido)
            else:
                error = 'Debe ingresar un apellido válido'
                
        elif edad:
            try: 
                edad = int(edad) #Por si no se introducen solo números
                futbolistas = Futbolista.objects.filter(edad = edad)
            except:
                error = 'Debe ingresar una edad válida'   
                         
    return render(request, 'AppCoder/lista_futbolistas.html', {'futbolistas': futbolistas, 'error': error})        

@login_required
def crear_futbolista(request):
    if request.method == 'POST':
        formulario = FutbolistasFormulario(request.POST)
        
        if formulario. is_valid():
            datos_futbolista = formulario.cleaned_data
            futbolista = Futbolista(nombre = datos_futbolista['nombre'], apellido = datos_futbolista['apellido'], edad = datos_futbolista['edad'])
            futbolista.save()
            return redirect('Futbolistas')
    formulario = FutbolistasFormulario()
        
    return render(request, 'AppCoder/formulario_futbolista.html', {'formulario': formulario})

def lista_basquetbolistas(request):
    basquetbolistas = None
    error = None
    if request.method =='GET':
        nombre = request.GET.get('nombre', '')
        apellido = request.GET.get('apellido','')
        triples = request.GET.get('triples',None)
        if nombre == '' and apellido == '' and triples == '' : #Se considera que si no introdujo ningún campo, está queriendo ver todos.
            basquetbolistas = Basquetbolista.objects.all()
        elif nombre: 
            if nombre.replace(' ','').isalpha():
                basquetbolistas = Basquetbolista.objects.filter(nombre = nombre)
            else:
                error = 'Debe ingresar un nombre válido'
        
        elif apellido:
            if apellido.replace(' ','').isalpha():
                basquetbolistas = Basquetbolista.objects.filter(apellido = apellido)
            else:
                error = 'Debe ingresar un apellido válido'
                
        elif triples:
            try: 
                triples = int(triples)
                basquetbolistas = Basquetbolista.objects.filter(triples = triples)
            except:
                error = 'Debe ingresar una cantidad de triples válida'   
                         
    return render(request, 'AppCoder/lista_basquetbolistas.html', {'basquetbolistas': basquetbolistas, 'error': error})

@login_required
def crear_basquetbolista(request):
    if request.method == 'POST':
        formulario = BasquetbolistasFormulario(request.POST)
        
        if formulario. is_valid():
            datos_basquetbolista = formulario.cleaned_data
            basquetbolista = Basquetbolista(nombre = datos_basquetbolista['nombre'], apellido = datos_basquetbolista['apellido'], triples = datos_basquetbolista['triples'])
            basquetbolista.save()
            return redirect('Basquetbolistas')
    formulario = BasquetbolistasFormulario()
        
    return render(request, 'AppCoder/formulario_basquetbolista.html', {'formulario': formulario})
    
def lista_tenistas(request):
    tenistas = None
    error = None
    if request.method =='GET':
        nombre = request.GET.get('nombre', '')
        apellido = request.GET.get('apellido','')
        titulos = request.GET.get('titulos',None)
        if nombre == '' and apellido == '' and titulos == '' : #Se considera que si no introdujo ningún campo, está queriendo ver todos.
            tenistas = Tenista.objects.all()
        elif nombre: 
            if nombre.replace(' ','').isalpha():
                tenistas = Tenista.objects.filter(nombre = nombre)
            else:
                error = 'Debe ingresar un nombre válido'
        
        elif apellido:
            if apellido.replace(' ','').isalpha():
                tenistas = Tenista.objects.filter(apellido = apellido)
            else:
                error = 'Debe ingresar un apellido válido'
                
        elif titulos:
            try: 
                titulos = int(titulos)
                tenistas = Tenista.objects.filter(titulos = titulos)
            except:
                error = 'Debe ingresar una cantidad de títulos válida'   
                         
    return render(request, 'AppCoder/lista_tenistas.html', {'tenistas': tenistas, 'error': error})        

@login_required
def crear_tenista(request):   
    if request.method == 'POST':
        formulario = TenistasFormulario(request.POST)
        
        if formulario. is_valid():
            datos_tenista = formulario.cleaned_data
            tenista = Tenista(nombre = datos_tenista['nombre'], apellido = datos_tenista['apellido'], titulos = datos_tenista['titulos'])
            tenista.save()
            return redirect('Tenistas')
    formulario = TenistasFormulario()
        
    return render(request, 'AppCoder/formulario_tenista.html', {'formulario': formulario})

class FutbolistaDetailView(DetailView):
    model = Futbolista
    template_name = "AppCoder/detalle_futbolista.html"
    fields = ['nombre', 'apellido', 'edad']
    
class BasquetbolistaDetailView(DetailView):
    model = Basquetbolista
    template_name = "AppCoder/detalle_basquetbolista.html"
    fields = ['nombre', 'apellido', 'triples']

class TenistaDetailView(DetailView):
    model = Tenista
    template_name = "AppCoder/detalle_tenista.html"
    fields = ['nombre', 'apellido', 'titulos']
    
class FutbolistaDeleteView(LoginRequiredMixin, DeleteView):
    model = Futbolista
    success_url = "/futbolistas/"
    template_name = "AppCoder/borrado_futbolista.html"

class BasquetbolistaDeleteView(LoginRequiredMixin, DeleteView):
    model = Basquetbolista
    success_url = "/basquetbolistas/"
    template_name = "AppCoder/borrado_basquetbolista.html"

class TenistaDeleteView(LoginRequiredMixin, DeleteView):
    model = Tenista
    success_url = "/tenistas/"
    template_name = "AppCoder/borrado_tenista.html"
    
class FutbolistaUpdateView(LoginRequiredMixin, UpdateView):
    model = Futbolista
    success_url = "/futbolistas/"
    fields = ['nombre', 'apellido', 'edad']
    template_name = "AppCoder/actualizado_futbolista.html"

class BasquetbolistaUpdateView(LoginRequiredMixin, UpdateView):
    model = Basquetbolista
    success_url = "/basquetbolistas/"
    fields = ['nombre', 'apellido', 'triples']
    template_name = "AppCoder/actualizado_basquetbolista.html"
    
class TenistaUpdateView(LoginRequiredMixin, UpdateView):
    model = Tenista
    success_url = "/tenistas/"
    fields = ['nombre', 'apellido', 'titulos']
    template_name = "AppCoder/actualizado_tenista.html"

def login_request(request):
    if request.method == 'POST':
        form = LoginAuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username, password=password)
            if username is not None:
                login(request, user)
                return render (request,'AppCoder/index.html', {'flag': True, 'mensaje': 'Te logueaste con éxito!'})
        else:
            return render (request,'AppCoder/login.html', {'form': form, 'mensaje': 'Error', 'error_user': True})
    form = LoginAuthenticationForm()
    return render(request, 'AppCoder/login.html', {'form': form, 'mensaje': '', 'error_user': False})

def register_request(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        
        if form.is_valid():
            form.save()
            return render (request, 'AppCoder/index.html', {'flag': True, 'mensaje': 'Te registraste con éxito!'})
        
        else:
            return render (request,'AppCoder/register.html', {'form': form, 'mensaje': 'Por favor, revisa los requisitos para crear el usuario.', 'error_user': True})
    form = RegistroUsuarioForm()
    return render(request, 'AppCoder/register.html', {'form': form, 'mensaje': '', 'error': False})

@login_required
def editar_user(request):
    usuario = request.user
    
    if request.method == 'POST':
        form = EditarUsuarioForm(request.POST)
        
        if form.is_valid():
            datos_usuario = form.cleaned_data
            usuario.email = datos_usuario ['email']
            usuario.set_password(datos_usuario ['password1']) #Paso necesario para cambiar contraseña
          
            usuario.save()
            
            return render (request, 'AppCoder/index.html', {'flag': True, 'mensaje': 'Usuario editado con éxito!'})
        
        else:
            
            return render (request,'AppCoder/editar_user.html', {'form': form, 'mensaje': 'Por favor, revisa los requisitos para editar el usuario.', 'error_user': True})
           
    form = EditarUsuarioForm(initial={'email': usuario.email})
    return render(request, 'AppCoder/editar_user.html', {'form': form, 'mensaje': '', 'error': False})

@login_required
def editar_avatar(request):
    user_avatar = Avatar.objects.filter (user=request.user.id)
    usuario = request.user
    
    if request.method == 'POST':
        form = AvatarForm(request.POST, request.FILES)
        
        if form.is_valid():
            try:
                avatar = Avatar.objects.get(user=usuario)
                avatar.avatar = form.cleaned_data['avatar']
            except:
                avatar = Avatar(user=usuario, avatar=form.cleaned_data['avatar'])
            avatar.save()
            return render (request, 'AppCoder/index.html', {'flag': True, 'mensaje': 'Avatar cargado con éxito!'})
    form = AvatarForm()
    try:
        return render(request, 'AppCoder/editar_avatar.html', {'form': form, 'mensaje': '', "url": user_avatar[0].avatar.url})
    except:
        return render(request, 'AppCoder/editar_avatar.html', {'form': form, 'mensaje': 'Estás a punto de cargar tu primer Avatar!'})
    
def about(request):
    return render(request, 'AppCoder/about.html', {})