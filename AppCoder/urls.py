from django.urls.conf import path
from django.contrib.auth.views import LogoutView

from .views import index, lista_futbolistas, lista_basquetbolistas, lista_tenistas, crear_futbolista, crear_basquetbolista, crear_tenista, login_request, register_request, editar_user, editar_avatar, about

from . import views

urlpatterns = [
    path('', index, name='index'),
    path('futbolistas/', lista_futbolistas, name='Futbolistas'),
    path('futbolistas/crear/', crear_futbolista, name='Crear_Futbolista'),
    path('basquetbolistas/', lista_basquetbolistas, name='Basquetbolistas'),
    path('basquetbolistas/crear', crear_basquetbolista, name='Crear_Basquetbolista'),
    path('tenistas/', lista_tenistas, name='Tenistas'),
    path('tenistas/crear', crear_tenista, name='Crear_Tenista'),
    path(r'futbolistas/detalle/<int:pk>', views.FutbolistaDetailView.as_view(), name='Detalle_Futbolista'),
    path(r'basquetbolistas/detalle/<int:pk>', views.BasquetbolistaDetailView.as_view(), name='Detalle_Basquetbolista'),
    path(r'tenistas/detalle/<int:pk>', views.TenistaDetailView.as_view(), name='Detalle_Tenista'),
    path(r'futbolistas/borrar/<int:pk>', views.FutbolistaDeleteView.as_view(), name='Borrar_Futbolista'),
    path(r'basquebolistas/borrar/<int:pk>', views.BasquetbolistaDeleteView.as_view(), name='Borrar_Basquetbolista'),
    path(r'tenistas/borrar/<int:pk>', views.TenistaDeleteView.as_view(), name='Borrar_Tenista'),
    path(r'futbolistas/actualizar/<int:pk>', views.FutbolistaUpdateView.as_view(), name='Actualizar_Futbolista'),
    path(r'basquetbolistas/actualizar/<int:pk>', views.BasquetbolistaUpdateView.as_view(), name='Actualizar_Basquetbolista'),
    path(r'tenistas/actualizar/<int:pk>', views.TenistaUpdateView.as_view(), name='Actualizar_Tenista'),
    path('login/', login_request, name='Login'),
    path('logout/', LogoutView.as_view(template_name='AppCoder/logout.html'), name='Logout'),
    path('register/', register_request, name='Register'),
    path('editar_user/', editar_user, name='Editar_User'), 
    path('editar_avatar/', editar_avatar, name='Editar_Avatar'), 
    path('about/', about, name='About'), 
    
]

