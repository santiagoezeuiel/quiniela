# Generated by Django 5.1.3 on 2024-11-14 14:29

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_local', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Genero')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creado')),
                ('updated', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de alta')),
            ],
            options={
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Tipo_telefono',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_created=True, verbose_name='Creado')),
                ('nombre', models.CharField(max_length=50, verbose_name='Tipo de telefono')),
                ('updated', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de alta')),
            ],
            options={
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Agenciero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.ImageField(upload_to='agenciero')),
                ('dni', models.CharField(help_text='Introduzca el DNI:', max_length=11, unique=True, validators=[django.core.validators.RegexValidator('^\\d+$')], verbose_name='D.N.I')),
                ('cuil', models.CharField(help_text='Introduzca en numero de C.U.I.L', max_length=14, unique=True, validators=[django.core.validators.RegexValidator('^\\d+$')], verbose_name='C.U.I.L')),
                ('cbu', models.CharField(help_text='Introduzca el numero de CBU', max_length=22, unique=True, validators=[django.core.validators.RegexValidator('^\\d{22}$')], verbose_name='CBU')),
                ('barrio', models.CharField(max_length=50, verbose_name='Nombre del Barrio')),
                ('calle', models.CharField(max_length=50, verbose_name='Nombre de calle')),
                ('n_casa', models.IntegerField(verbose_name='Numero de casa')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creado')),
                ('updated', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de alta')),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_local.departamento', verbose_name='Departamento')),
                ('localidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_local.localidad', verbose_name='Localidad')),
                ('provincia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_local.provincia', verbose_name='Provincia')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
                ('genero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_agenciero.genero', verbose_name='Genero')),
            ],
            options={
                'ordering': ('-id', 'user'),
            },
        ),
    ]
