# Generated by Django 5.1.3 on 2024-11-14 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_agenciero', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agenciero',
            name='created',
        ),
        migrations.RemoveField(
            model_name='agenciero',
            name='updated',
        ),
    ]
