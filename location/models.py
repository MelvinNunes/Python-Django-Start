from django.db import models
from django.conf import settings
# Create your models here.


class Provincia(models.Model):
    nome_provincia = models.CharField(
        max_length=255, unique=True, null=False)
    acronimo = models.CharField(max_length=3, unique=True)
    createdBy = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, related_name='ProvinciaCreatedBy')
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    updatedBy = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, related_name='ProvinciaUpdatedBy')


class Distrito(models.Model):
    provincia = models.ForeignKey(
        Provincia, on_delete=models. CASCADE)
    nome_distrito = models.CharField(
        max_length=255, unique=True, null=False)
    createdBy = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, related_name='DistritoCreatedBy')
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    updatedBy = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, related_name='DistritoUpdatedBy')


class Bairro(models.Model):
    distrito = models.ForeignKey(
        Distrito, on_delete=models.CASCADE)
    nome_bairro = models.CharField(max_length=255, unique=True, null=False)
    createdBy = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True,  related_name='BairroCreatedBy')
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    updatedBy = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, related_name='BairroUpdatedBy')
