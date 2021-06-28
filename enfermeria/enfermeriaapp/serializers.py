from rest_framework import serializers
from enfermeriaapp.models import Persona, Tranresponse, Usuario, Servicio, Reserva, ReservaXServicio

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = ['id', 'per_nombre', 'per_apellidoP', 'per_apellidoM', 'per_celular', 'per_ci', 'per_direccion', 'per_email', 'per_sexo', 'per_estado']

class TranResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tranresponse
        fields = ['id', 'tran_data', 'tran_exito', 'tran_msg']

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'usu_username', 'usu_password', 'usu_estado', 'usu_per']

class ServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicio
        fields = ['id', 'ser_nombre', 'ser_desc', 'ser_precio', 'ser_estado']

class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = ['id', 'res_fechaReserva', 'res_horaReserva', 'res_fechaServicio', 'res_horaServicio', 'res_lat', 'res_lng', 'res_estadoRes', 'res_estado', 'res_persona']

class ReservaXServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReservaXServicio
        fields = ['id', 'res', 'ser', 'cant']