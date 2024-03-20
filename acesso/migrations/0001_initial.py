# Generated by Django 5.0.3 on 2024-03-20 03:02

import django.db.models.deletion
import django.utils.timezone
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Chave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disponivel', models.BooleanField(default=True, verbose_name='Disponivel')),
                ('qr_code', models.ImageField(blank=True, null=True, upload_to='qr_codes/')),
            ],
            options={
                'verbose_name': 'Chave',
                'verbose_name_plural': 'Chaves',
                'ordering': ['sala'],
            },
        ),
        migrations.CreateModel(
            name='Predio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('rua', models.CharField(max_length=100, verbose_name='Rua')),
                ('bairro', models.CharField(max_length=100, verbose_name='Bairro')),
                ('cidade', models.CharField(max_length=100, verbose_name='Cidade')),
                ('cep', models.CharField(max_length=10, verbose_name='CEP')),
                ('telefone', models.CharField(max_length=18, verbose_name='Telefone')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
            ],
            options={
                'verbose_name': 'Prédio',
                'verbose_name_plural': 'Prédios',
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('cpf', models.CharField(blank=True, max_length=11, null=True)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='avatares', verbose_name='Foto')),
                ('funcao', models.CharField(blank=True, max_length=50, null=True)),
                ('telefone', models.CharField(blank=True, max_length=20, null=True)),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='funcionario', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Funcionário',
                'verbose_name_plural': 'Funcionários',
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Aluguel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_aluguel', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data da Retirada da Chave')),
                ('data_devolucao', models.DateTimeField(blank=True, null=True, verbose_name='Data da devolução')),
                ('numero', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('chave', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='alugueis', to='acesso.chave')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='usuario_alugueis', to='acesso.funcionario')),
            ],
            options={
                'verbose_name': 'Aluguél',
                'verbose_name_plural': 'Aluguéis',
                'ordering': ['numero'],
            },
        ),
        migrations.CreateModel(
            name='Sala',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=50, verbose_name='Descrição')),
                ('numero', models.CharField(max_length=10, verbose_name='Número da Sala')),
                ('predio', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='acesso.predio', verbose_name='Prédio')),
            ],
            options={
                'verbose_name': 'Sala',
                'verbose_name_plural': 'Salas',
                'ordering': ['numero'],
            },
        ),
        migrations.AddField(
            model_name='chave',
            name='sala',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chaves', to='acesso.sala'),
        ),
    ]
