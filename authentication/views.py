from functools import partial
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.models import Group
from authentication.models import User
from .serializers import MyRefreshTokenSerializer, MyTokenObtainPairSerializer, UsersSerializer
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from .permission import IsAdminUser, IsAdminOrSeguradoraUser, IsAdminOrClientUser, IsAdminOrSeguradoraOrDelegacaoUser
# Create your views here.


# JWT

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class MyTokenRefreshView(TokenRefreshView):
    serializer_class = MyRefreshTokenSerializer


# Views

class Admin_View(APIView):
    permission_classes = [permissions.IsAuthenticated, IsAdminUser]

    def post(self, request,  *args, **kwargs):
        serializer_user = UsersSerializer(data=request.data)
        if serializer_user.is_valid(raise_exception=True):
            password = serializer_user.validated_data.pop('password', None)
            instance = serializer_user.save()
            if password is not None:
                instance.set_password(password)
                username = serializer_user.validated_data.get('username')
                obj = get_object_or_404(User, username=username)
                instance.owner = obj
                g = Group.objects.get(name='admin')
                instance.groups.add(g)
            serializer_user.save()
            return Response(serializer_user.data)


class Cliente_View(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request,  *args, **kwargs):
        serializer_user = UsersSerializer(data=request.data)
        if serializer_user.is_valid(raise_exception=True):
            password = serializer_user.validated_data.pop('password', None)
            instance = serializer_user.save()
            if password is not None:
                instance.set_password(password)
                username = serializer_user.validated_data.get('username')
                obj = get_object_or_404(User, username=username)
                instance.owner = obj
                g = Group.objects.get(name='client')
                instance.groups.add(g)
            serializer_user.save()
            return Response(serializer_user.data)


class Seguradora_Manager_View(APIView):
    permission_classes = [permissions.IsAuthenticated, IsAdminUser]

    def post(self, request,  *args, **kwargs):
        serializer_user = UsersSerializer(data=request.data)
        if serializer_user.is_valid(raise_exception=True):
            password = serializer_user.validated_data.pop('password', None)
            instance = serializer_user.save()
            if password is not None:
                instance.set_password(password)
                username = serializer_user.validated_data.get('username')
                obj = get_object_or_404(User, username=username)
                instance.owner = obj
                g = Group.objects.get(name='seguradora_managers')
                instance.groups.add(g)
            serializer_user.save()
            return Response(serializer_user.data)


class Delegacao_Manager(APIView):
    permission_classes = [permissions.IsAuthenticated, IsAdminOrSeguradoraUser]

    def post(self, request,  *args, **kwargs):
        serializer_user = UsersSerializer(data=request.data)
        if serializer_user.is_valid(raise_exception=True):
            password = serializer_user.validated_data.pop('password', None)
            instance = serializer_user.save()
            if password is not None:
                instance.set_password(password)
                instance.is_delegacao_manager = True
                username = serializer_user.validated_data.get('username')
                obj = get_object_or_404(User, username=username)
                instance.owner = obj
                g = Group.objects.get(name='delegacao_managers')
                instance.groups.add(g)
            serializer_user.save()
            return Response(serializer_user.data)

# Get my User


class GetMyUserView(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        obj = get_object_or_404(User, owner=request.user)
        data = UsersSerializer(obj, many=False).data
        return Response(data)

    def put(self, request,  *args, **kwargs):
        id = request.data.get("id")
        if id is not None:
            obj = get_object_or_404(User, id=id)
        else:
            return Response({"error": "no id given"}, status=404)
        if request.user == obj:
            serializer = UsersSerializer(
                obj, data=request.data, many=False, partial=True)
            if serializer.is_valid(raise_exception=True):
                # User update personal data
                serializer.save()
                # User Password
                password = serializer.validated_data.pop(
                    'password', None)
                instance = serializer.save()
                if password is not None:
                    instance.set_password(password)
                return Response(serializer.data)
        return Response({"error": 'Denied. Not Owner!'}, status=401)

    def delete(self, request,  *args, **kwargs):
        id = request.data.get("id")
        if id is not None:
            obj = get_object_or_404(User, id=id)
            if request.user == obj.id:
                obj.delete()
                return Response({"sucess": 'Deleted sucessfully'})
            return Response({"error": 'Denied. Not Owner!'}, status=401)

# Admin


class GetAllUsersView(APIView):

    permission_classes = [permissions.IsAuthenticated, IsAdminUser]

    def get(self, request, *args, **kwargs):
        queryset = User.objects.all()
        data = UsersSerializer(queryset, many=True).data
        return Response(data)
