# Generated by Django 4.1.1 on 2022-10-24 07:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Provincia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_provincia', models.CharField(max_length=255, unique=True)),
                ('acronimo', models.CharField(max_length=3, unique=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('createdBy', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ProvinciaCreatedBy', to=settings.AUTH_USER_MODEL)),
                ('updatedBy', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ProvinciaUpdatedBy', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Distrito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_distrito', models.CharField(max_length=255, unique=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('createdBy', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='DistritoCreatedBy', to=settings.AUTH_USER_MODEL)),
                ('provincia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='location.provincia')),
                ('updatedBy', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='DistritoUpdatedBy', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Bairro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_bairro', models.CharField(max_length=255, unique=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('createdBy', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='BairroCreatedBy', to=settings.AUTH_USER_MODEL)),
                ('distrito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='location.distrito')),
                ('updatedBy', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='BairroUpdatedBy', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]