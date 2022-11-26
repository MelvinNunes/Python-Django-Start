from rest_framework import serializers

from .models import Bairro, Distrito, Provincia


class Bairro_Serializer(serializers.ModelSerializer):
    nome_distrito = serializers.CharField(
        source='distrito.nome_distrito', read_only=True)

    class Meta:
        model = Bairro
        fields = ['id', 'distrito', 'nome_distrito', 'nome_bairro']

        extra_kwargs = {
            "distrito": {
                "write_only": True
            }
        }


class Provincia_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Provincia
        fields = ['id', 'nome_provincia', 'acronimo']


class Distrito_Serializer(serializers.ModelSerializer):
    nome_provincia = serializers.CharField(
        source='provincia.nome_provincia', read_only=True)

    class Meta:
        model = Distrito
        fields = ['id', 'nome_provincia', 'provincia', 'nome_distrito']

        extra_kwargs = {
            "provincia": {
                "write_only": True
            }
        }
