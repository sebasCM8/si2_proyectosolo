from rest_framework import serializers
from enfermeriaapp.models import Persona, Tranresponse, Usuario

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