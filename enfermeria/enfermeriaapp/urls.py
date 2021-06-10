from django.urls import path 
from . import views

app_name = 'enfermeriaapp'
urlpatterns = [
    path('homePage/', views.homePage_view, name="homepage_view"),
    path('loginPage/', views.login_view, name="login_view"),
    path('registrarPersona/', views.registrar_persona_view, name="registrar_persona_view")
]
