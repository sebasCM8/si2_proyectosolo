from django.urls import path 
from . import views

app_name = 'enfermeriaapp'
urlpatterns = [
    path('homePage/', views.homePage_view, name="homepage_view"),
    path('loginPage/', views.login_view, name="login_view"),
    path('registrarPersona/', views.registrar_persona_view, name="registrar_persona_view"),
    path('perfil/', views.perfil_view, name="perfil_view"),
    path('gestionar_personal/', views.gestionar_personal_view, name="gestionar_personal_view"),
    path('ver_personal/', views.ver_personal_view, name="ver_personal_view"),
    path('gestionar_servicios/', views.gestionar_servicios_view, name="gestionar_servicios_view"),
    path('registrar_servicio/', views.registrar_servicio_view, name="registrar_servicio_view")
]
