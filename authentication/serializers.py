from unicodedata import name
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer
from authentication.models import User
from django.contrib.auth.models import Group

################JWT CUSTOM CLAIMS############


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('name',)


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        queryset = user.groups.all()
        roles = GroupSerializer(queryset, many=True).data

        # Add custom claims
        token['first_name'] = user.first_name
        token['last_name'] = user.last_name
        token['roles'] = roles

        # ...

        return token


class MyRefreshTokenSerializer(TokenRefreshSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['first_name'] = user.first_name
        token['last_name'] = user.last_name
        # ...

        return token


# USER

class UsersSerializer (serializers.ModelSerializer):
    groups = GroupSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id',  'username', 'password',
                  'first_name', 'last_name', 'email', 'birth_date',
                  'contact_1', 'contact_2', 'contact_3', 'address', 'groups']

        extra_kwargs = {
            "password": {'write_only': True},
        }
