from django.contrib import admin
from django.urls import path, include
from AppProyecto import views
from django.contrib.auth.views import LogoutView 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name="Inicio"),
    path('tazas', views.listar_tazas, name="Tazas"),
    path('funkos', views.listar_funkos, name="Funkos"),
    path('remeras', views.listar_remeras, name="Remeras"),
    path('sobremi', views.sobre_mi, name="SobreMi"),
    path('crear_taza', views.crear_taza, name="TazasFormulario"),
    path('crear_funko', views.crear_funko, name="FunkosFormulario"),
    path('crear_remera', views.crear_remera, name="RemerasFormulario"),
    path('editar_taza/<taza_nombre>', views.editar_taza, name="EditarTaza"),
    path('editar_funko/<funko_nombre>', views.editar_funko, name="EditarFunko"),
    path('editar_remera/<remera_nombre>', views.editar_remera, name="EditarRemera"),
    path('eliminar_taza/<taza_nombre>/', views.eliminar_taza, name="EliminarTaza"),
    path('eliminar_funko/<funko_nombre>/', views.eliminar_funko, name="EliminarFunko"),
    path('eliminar_remera/<remera_nombre>/', views.eliminar_remera, name="EliminarRemera"),
    path('taza_detalle/<taza_id>/', views.taza_detalle, name='TazaDetalle'),
    path('funko_detalle/<funko_id>/', views.funko_detalle, name='FunkoDetalle'),
    path('remera_detalle/<remera_id>/', views.remera_detalle, name='RemeraDetalle'),
    path('register', views.register, name='Registro'),
    path('login', views.login_request, name="Login"),
    path('logout', LogoutView.as_view(template_name='AppProyecto/logout.html'), name='Logout'),
    path('editar_perfil', views.editar_perfil, name="EditarPerfil"),
    path('resultado_busqueda_taza/', views.buscar_tazas, name="ResultadoBusquedaTaza"),
    path('resultado_busqueda_funko/', views.buscar_funkos, name="ResultadoBusquedaFunko"),
    path('resultado_busqueda_remera/', views.buscar_remeras, name="ResultadoBusquedaRemera"),
]