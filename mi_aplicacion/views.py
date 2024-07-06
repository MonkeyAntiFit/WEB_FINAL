
from django.shortcuts import render, redirect, get_object_or_404
from .models import usuario, candidato, Producto, CarritoItem
from django.contrib import messages
from django.db import IntegrityError
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import ProductoForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test

def index(request):
    context={}
    return render(request, 'index.html', context)

def skate(request):
    productos = Producto.objects.filter(categoria='skate')
    return render(request, 'skate.html', {'productos': productos})

def roller(request):
    productos = Producto.objects.filter(categoria='roller')
    return render(request, 'roller.html', {'productos': productos})

def surf(request):
    productos = Producto.objects.filter(categoria='surf')
    return render(request, 'surf.html', {'productos': productos})

def accesorioroller(request):
    productos = Producto.objects.filter(categoria='accesorioroller')
    return render(request, 'accesorioroller.html', {'productos': productos})

def accesorioskate(request):
    productos = Producto.objects.filter(categoria='accesorioskate')
    return render(request, 'accesorioskate.html', {'productos': productos})

def accesoriosurf(request):
    productos = Producto.objects.filter(categoria='accesoriosurf')
    return render(request, 'accesoriosurf.html', {'productos': productos})

def loginNuevo(request):
    context={}
    return render(request, 'loginNuevo.html', context)

def registroUser(request):
    context={}
    return render(request, 'registroUser.html', context)

def mapa(request):
    context={}
    return render(request, 'mapa.html', context)

def trabajaConNosotros(request):
    context={}
    return render(request, 'trabajaConNosotros.html', context)

def spots(request):
    context={}
    return render(request, 'spots.html', context)

def is_admin(user):
    return user.is_authenticated and user.is_staff

def agregar_al_carrito(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        quantity = int(request.POST.get('quantity', 1))
        

        producto = Producto.objects.get(id=product_id)
        carrito, created = Carrito.objects.get_or_create(usuario=request.user)
        carrito.productos.add(producto, through_defaults={'cantidad': quantity})
        
        
        carrito_data = carrito.get_carrito_data()
        
        return JsonResponse({'success': True, 'carrito': carrito_data})
    
    return JsonResponse({'success': False}, status=400)

def eliminar_del_carrito(request, producto_id):
    carrito_item = get_object_or_404(CarritoItem, producto_id=producto_id)
    carrito_item.delete()
    return redirect('ver_carrito')

def ver_carrito(request):
    carrito = CarritoItem.objects.all()
    total = sum(item.producto.precio * item.cantidad for item in carrito)
    return render(request, 'carrito_content.html', {'carrito': carrito, 'total': total})
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('correo')
        password = request.POST.get('contraseña')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  
            messages.error(request, 'Correo o contraseña incorrectos')
    return render(request, 'loginNuevo.html')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Cuenta creada para {username}')
            return redirect('login')  
    else:
        form = UserCreationForm()
    return render(request, 'registroUser.html', {'form': form})

@login_required
@user_passes_test(is_admin)
def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto agregado exitosamente.')
            return redirect('lista_productos')
    else:
        form = ProductoForm()
    return render(request, 'agregar_producto.html', {'form': form})

@login_required
@user_passes_test(is_admin)
def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'lista_productos.html', {'productos': productos})

@login_required
@user_passes_test(is_admin)
def editar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto actualizado exitosamente.')
            return redirect('lista_productos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'editar_producto.html', {'form': form})

@login_required
@user_passes_test(is_admin)
def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        producto.delete()
        messages.success(request, 'Producto eliminado exitosamente.')
        return redirect('lista_productos')
    return render(request, 'eliminar_producto.html', {'producto': producto})

def agregarUsuario(request):
    if request.method == "POST":
        if request.POST['contrasena'] == request.POST['confirmarContrasena']:
            try:
                user = User.objects.create_user(
                                                username=request.POST['usuario'],
                                                password=request.POST['contrasena'],
                                                email=request.POST['correo'],
                                                first_name=request.POST['nombre'],
                                                last_name=request.POST['apellido'])
                user.save()
                usu = usuario.objects.create(
                    nombre_usuario=request.POST["usuario"],
                    nombre=request.POST["nombre"],
                    apellido=request.POST["apellido"],
                    rut=request.POST["rut"],
                    correo=request.POST["correo"],
                    contrasena=request.POST["contrasena"] 
                )
                usu.save()
                return render(request,'registroUser.html',context)
            except:
                return render(request,'registroUser.html',{
                    'error':'Nombre de usuario ya existe.'
                })
        else:
            return render(request,'registroUser.html',{'error': 'Contraseñas no coinciden.'})
    else:
        context={}
    return render(request,'registroUser.html',context)

def registroCandidato(request):
    if request.method == 'POST':
        nombreCandidato = request.POST['nombreCandidato']
        apellidoCandidato = request.POST['apellidoCandidato']
        correo = request.POST['correo']
        rut = request.POST['rut']
        edad = request.POST['edad']
        terminos = request.POST.get('terminos', False)

        if terminos:
            try:
                nuevo_candidato = candidato(
                   nombreCandidato = nombreCandidato,
                   apellidoCandidato = apellidoCandidato,
                   correo = correo,
                   rut = rut,
                   edad = edad 
                )
                nuevo_candidato.save()
                messages.success(request, 'Datos agregados con exito.')
                return redirect('index')
            except IntegrityError:
                messages.error(request, 'El rut ya está en uso. Por favor, intenta con otro.')
        else:
            messages.error(request, 'Debes aceptar los términos y condiciones.')
    return render(request, 'registroUser.html')