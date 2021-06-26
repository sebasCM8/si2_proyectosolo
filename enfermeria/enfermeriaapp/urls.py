from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'enfermeriaapp'
urlpatterns = [
    path('homePage/', views.homePage_view, name="homepage_view"),
    path('loginPage/', views.login_view, name="login_view"),
    path('registrarPersona/', views.registrar_persona_view, name="registrar_persona_view"),
    path('perfil/', views.perfil_view, name="perfil_view"),
    path('gestionar_personal/', views.gestionar_personal_view, name="gestionar_personal_view"),
    path('ver_personal/', views.ver_personal_view, name="ver_personal_view"),
    path('gestionar_servicios/', views.gestionar_servicios_view, name="gestionar_servicios_view"),
    path('registrar_servicio/', views.registrar_servicio_view, name="registrar_servicio_view"),
    path('editar_servicio/', views.editar_servicio_view, name="editar_servicio_view"),
    path('eliminar_servicio/', views.eliminar_servicio_view, name="eliminar_servicio_view"),
    path('api_personas/', views.persona_list),
    path('api_persona/<int:pk>/', views.persona_detail),
    path('api_persona_ci/<int:ci>/', views.get_persona_ci),
    path('api_register_usuario/', views.register_user),
    path('api_get_user_username/<str:username>/', views.get_user_username)
]

urlpatterns = format_suffix_patterns(urlpatterns)