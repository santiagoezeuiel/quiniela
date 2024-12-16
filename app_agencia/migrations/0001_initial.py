# Generated by Django 5.1.3 on 2024-11-14 16:22

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
            name='Activo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='Activa', max_length=50, verbose_name='Estado de la agencia')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creado')),
                ('updated', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de alta')),
            ],
            options={
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Agencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('n_agencia', models.IntegerField(verbose_name='Numero de agencia')),
                ('barrio', models.CharField(max_length=50, verbose_name='Barrio')),
                ('n_casa', models.IntegerField(verbose_name='Numero de casa')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creado')),
                ('updated', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de alta')),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_local.departamento', verbose_name='Departamento')),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_agencia.activo', verbose_name='Estado de la agencia')),
                ('localidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_local.localidad', verbose_name='Localidad')),
                ('provincia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_local.provincia', verbose_name='Provincia')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('id', 'n_agencia'),
            },
        ),
    ]