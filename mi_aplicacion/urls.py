from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.index, name='index'),
    path('skate/', views.skate, name='skate'),
    path('roller/', views.roller, name='roller'),
    path('surf/', views.surf, name='surf'),
    path('accesorioroller/', views.accesorioroller, name='accesorioroller'),
    path('accesorioskate/', views.accesorioskate, name='accesorioskate'),
    path('accesoriosurf/', views.accesoriosurf, name='accesoriosurf'),
    path('mapa/', views.mapa, name='mapa'),
    path('trabaja-con-nosotros/', views.trabajaConNosotros, name='trabajaConNosotros'),
    path('spots/', views.spots, name='spots'),
    path('carrito/', views.ver_carrito, name='ver_carrito'),
    path('carrito/agregar/<int:producto_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('carrito/eliminar/<int:producto_id>/', views.eliminar_del_carrito, name='eliminar_del_carrito'),
    path('login/', views.login_view, name='login'),
    path('agregarUsuario', views.agregarUsuario, name='agregarUsuario'),
    path('agregar/', views.agregar_producto, name='agregar_producto'),
    path('productos/', views.lista_productos, name='lista_productos'),
    path('productos/editar/<int:producto_id>/', views.editar_producto, name='editar_producto'),
    path('productos/eliminar/<int:producto_id>/', views.eliminar_producto, name='eliminar_producto'),
    path('logout/', LogoutView.as_view(next_page='index'), name='logout'),
    path('loginNuevo', views.loginNuevo, name='loginNuevo'),
]
