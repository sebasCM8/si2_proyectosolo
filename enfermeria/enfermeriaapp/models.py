from django.db import models

# Create your models here.
class Persona(models.Model):
    per_nombre = models.CharField(max_length=30)
    per_apellidoP = models.CharField(max_length=30, null=True)
    per_apellidoM = models.CharField(max_length=30, null=True)
    per_celular = models.CharField(max_length=12, null=True)
    per_ci = models.CharField(max_length=12)
    per_direccion = models.CharField(max_length=80, null=True)
    per_email = models.CharField(max_length=50, null=True)
    per_sexo = models.CharField(max_length=1)
    per_estado = models.IntegerField()

class Usuario(models.Model):
    usu_username = models.CharField(max_length=30)
    usu_password = models.CharField(max_length=30)
    usu_estado = models.IntegerField()

    usu_per = models.ForeignKey(Persona, on_delete=models.CASCADE)

    def es_admin(self):
        the_admin = Administrador.objects.filter(adm_estado=1, adm_per=self.usu_per)
        if len(the_admin) == 1: return True
        return False
    def es_enfermero(self):
        the_nurse = Enfermero.objects.filter(enf_estado=1, enf_per=self.usu_per)
        if len(the_nurse) == 1: return True
        return False


class Administrador(models.Model):
    adm_estado = models.IntegerField()

    adm_per = models.ForeignKey(Persona, on_delete=models.CASCADE)

class Enfermero(models.Model):
    enf_estado = models.IntegerField()

    enf_per = models.ForeignKey(Persona, on_delete=models.CASCADE)


class Servicio(models.Model):
    ser_nombre = models.CharField(max_length=40)
    ser_desc = models.CharField(max_length=80)
    ser_precio = models.DecimalField(max_digits=7,decimal_places=2)
    ser_estado = models.IntegerField()


class Reserva(models.Model):
    res_fechaReserva = models.DateField(auto_now=True)
    res_horaReserva = models.TimeField(auto_now=True)
    res_fechaServicio = models.DateField()
    res_horaServicio = models.TimeField()
    res_lat = models.FloatField()
    res_lng = models.FloatField()
    res_estadoRes = models.IntegerField()
    res_estado = models.IntegerField()

    res_persona = models.ForeignKey(Persona, on_delete=models.CASCADE, null=True)
    res_enfermero = models.ForeignKey(Enfermero, on_delete=models.CASCADE, null=True)

    res_servicios = models.ManyToManyField(Servicio, through='ReservaXServicio')

class ReservaXServicio(models.Model):
    res = models.ForeignKey(Reserva, on_delete=models.CASCADE)
    ser = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    cant = models.IntegerField(null=True)

class Tranresponse(models.Model):
    tran_data = models.IntegerField()
    tran_exito = models.IntegerField()
    tran_msg = models.CharField(max_length=40, null=True)





