# Generated by Django 5.0.3 on 2024-03-20 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acesso', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='predio',
            name='numero',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Número'),
        ),
        migrations.AlterField(
            model_name='predio',
            name='rua',
            field=models.CharField(max_length=100, verbose_name='Logradouro'),
        ),
    ]
