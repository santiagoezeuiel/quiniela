# Generated by Django 5.1.3 on 2024-11-14 13:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Departamento')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creado')),
                ('updated', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de alta')),
            ],
            options={
                'ordering': ('id', 'provincia'),
            },
        ),
        migrations.CreateModel(
            name='Provincia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField(auto_created=True, verbose_name='Fecha de alta')),
                ('nombre', models.CharField(max_length=50, verbose_name='Provincia')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creado')),
            ],
            options={
                'ordering': ('id', 'nombre'),
            },
        ),
        migrations.CreateModel(
            name='Localidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Localidad')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creado')),
                ('updated', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de alta')),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_local.departamento', verbose_name='Departamento')),
            ],
            options={
                'ordering': ('id', 'departamento'),
            },
        ),
        migrations.AddField(
            model_name='departamento',
            name='provincia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_local.provincia', verbose_name='Provincia'),
        ),
    ]