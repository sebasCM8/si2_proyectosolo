# Generated by Django 3.2.3 on 2021-06-03 15:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Atencion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ate_estado', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('per_nombre', models.CharField(max_length=30)),
                ('per_apellidoP', models.CharField(max_length=30, null=True)),
                ('per_apellidoM', models.CharField(max_length=30, null=True)),
                ('per_celular', models.CharField(max_length=12, null=True)),
                ('per_ci', models.CharField(max_length=12)),
                ('per_direccion', models.CharField(max_length=80, null=True)),
                ('per_email', models.CharField(max_length=50, null=True)),
                ('per_sexo', models.CharField(max_length=1)),
                ('per_estado', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('res_fechaReserva', models.DateField(auto_now=True)),
                ('res_horaReserva', models.TimeField(auto_now=True)),
                ('res_fechaServicio', models.DateField()),
                ('res_horaServicio', models.TimeField()),
                ('res_lat', models.FloatField()),
                ('res_lng', models.FloatField()),
                ('res_estadoRes', models.IntegerField()),
                ('res_estado', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ser_nombre', models.CharField(max_length=40)),
                ('ser_desc', models.CharField(max_length=80)),
                ('ser_precio', models.DecimalField(decimal_places=2, max_digits=7)),
                ('ser_estado', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usu_username', models.CharField(max_length=30)),
                ('usu_password', models.CharField(max_length=30)),
                ('usu_estado', models.IntegerField()),
                ('usu_per', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enfermeriaapp.persona')),
            ],
        ),
        migrations.CreateModel(
            name='ReservaXAtencion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enfermeriaapp.atencion')),
                ('res', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enfermeriaapp.reserva')),
            ],
        ),
        migrations.AddField(
            model_name='reserva',
            name='res_atenciones',
            field=models.ManyToManyField(through='enfermeriaapp.ReservaXAtencion', to='enfermeriaapp.Atencion'),
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pac_estado', models.IntegerField()),
                ('pac_per', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enfermeriaapp.persona')),
            ],
        ),
        migrations.CreateModel(
            name='Enfermero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enf_estado', models.IntegerField()),
                ('enf_per', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enfermeriaapp.persona')),
            ],
        ),
        migrations.CreateModel(
            name='AtencionXServicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enfermeriaapp.atencion')),
                ('ser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enfermeriaapp.servicio')),
            ],
        ),
        migrations.AddField(
            model_name='atencion',
            name='ate_per',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enfermeriaapp.persona'),
        ),
        migrations.AddField(
            model_name='atencion',
            name='ate_servicios',
            field=models.ManyToManyField(through='enfermeriaapp.AtencionXServicio', to='enfermeriaapp.Servicio'),
        ),
        migrations.CreateModel(
            name='Administrador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adm_estado', models.IntegerField()),
                ('adm_per', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enfermeriaapp.persona')),
            ],
        ),
    ]
