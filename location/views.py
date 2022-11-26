from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response

from authentication.permission import IsAdminUser
from .models import Provincia, Bairro, Distrito
from .serializers import Provincia_Serializer, Bairro_Serializer, Distrito_Serializer
# Create your views here.


# Provincia

class Provincia_View(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request,  *args, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            obj = get_object_or_404(Provincia, id=id)
            data = Provincia_Serializer(obj, many=False).data
            return Response(data)
        queryset = Provincia.objects.all()
        data = Provincia_Serializer(queryset, many=True).data
        return Response(data)


class Provincia_Admin_View(APIView):
    permission_classes = [permissions.IsAuthenticated, IsAdminUser]

    def post(self, request,  *args, **kwargs):
        serializer = Provincia_Serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            acronimo_provincia = serializer.validated_data.get('acronimo')
            new_acron = acronimo_provincia.upper()
            serializer.save(createdBy=request.user, acronimo=new_acron)
            return Response(serializer.data)

    def put(self, request,  *args, **kwargs):
        id = request.data.get("id")
        if id is not None:
            obj = get_object_or_404(Provincia, id=id)
        else:
            return Response({"error": "no id given"}, status=404)
        serializer = Provincia_Serializer(obj, data=request.data, many=False)
        if serializer.is_valid(raise_exception=True):
            serializer.update(
                instance=obj, validated_data=serializer.validated_data)
            return Response({"sucess": 'Updated Sucessfully'})

    def delete(self, request,  *args, **kwargs):
        id = request.data.get("id")
        if id is not None:
            obj = get_object_or_404(Provincia, id=id)
            obj.delete()
            return Response({'sucess': 'Deleted sucessfully'})
        return Response({'error': 'Not Found'}, status=404)

# Distrito


class Distrito_View(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request,  *args, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            obj = get_object_or_404(Distrito, id=id)
            data = Distrito_Serializer(obj, many=False).data
            return Response(data)
        queryset = Distrito.objects.all()
        data = Distrito_Serializer(queryset, many=True).data
        return Response(data)


class Distrito_Admin_View(APIView):
    permission_classes = [permissions.IsAuthenticated, IsAdminUser]

    def post(self, request,  *args, **kwargs):
        serializer = Distrito_Serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(createdBy=request.user)
            return Response(serializer.data)

    def put(self, request,  *args, **kwargs):
        id = request.data.get("id")
        if id is not None:
            obj = get_object_or_404(Distrito, id=id)
        else:
            return Response({"error": "no id given"}, status=404)
        serializer = Distrito_Serializer(obj, data=request.data, many=False)
        if serializer.is_valid(raise_exception=True):
            serializer.update(
                instance=obj, validated_data=serializer.validated_data)
            return Response({"sucess": 'Updated Sucessfully'})

    def delete(self, request,  *args, **kwargs):
        id = request.data.get("id")
        if id is not None:
            obj = get_object_or_404(Distrito, id=id)
            obj.delete()
            return Response({'sucess': 'Deleted sucessfully'})
        return Response({'error': 'Not Found'}, status=404)

# Bairro


class Bairro_View(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request,  *args, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            obj = get_object_or_404(Bairro, id=id)
            data = Bairro_Serializer(obj, many=False).data
            return Response(data)
        queryset = Bairro.objects.all()
        data = Bairro_Serializer(queryset, many=True).data
        return Response(data)


class Bairro_Admin_View(APIView):
    permission_classes = [permissions.IsAuthenticated, IsAdminUser]

    def post(self, request,  *args, **kwargs):
        serializer = Bairro_Serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(createdBy=request.user)
            return Response(serializer.data)

    def put(self, request,  *args, **kwargs):
        id = request.data.get("id")
        if id is not None:
            obj = get_object_or_404(Bairro, id=id)
        else:
            return Response({"error": "no id given"}, status=404)
        serializer = Bairro_Serializer(obj, data=request.data, many=False)
        if serializer.is_valid(raise_exception=True):
            serializer.update(
                instance=obj, validated_data=serializer.validated_data)
            return Response({"sucess": 'Updated Sucessfully'})

    def delete(self, request,  *args, **kwargs):
        id = request.data.get("id")
        if id is not None:
            obj = get_object_or_404(Bairro, id=id)
            obj.delete()
            return Response({'sucess': 'Deleted sucessfully'})
        return Response({'error': 'Not Found'}, status=404)
