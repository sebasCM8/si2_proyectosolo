# Generated by Django 3.2.4 on 2021-06-25 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enfermeriaapp', '0002_auto_20210625_1327'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tranresponse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tran_data', models.IntegerField()),
                ('tran_exito', models.IntegerField()),
                ('tran_msg', models.CharField(max_length=40, null=True)),
            ],
        ),
    ]
