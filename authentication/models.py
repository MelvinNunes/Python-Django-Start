from django.db import models
from django.contrib.auth.models import AbstractUser, Group
from django.conf import settings
import os
from datetime import datetime

# Create your models here.


def filepath_avatar(request, filename):
    old_filename = filename
    time_now = datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = '%s%s' % (time_now, old_filename)
    return os.path.join('uploads/usuarios/avatar', filename)


class User(AbstractUser):
    first_name = models.CharField(max_length=255, null=False)
    last_name = models.CharField(max_length=255, null=False)
    email = models.EmailField(unique=True)
    birth_date = models.DateField(null=True)
    contact_1 = models.CharField(max_length=255, null=False)
    contact_2 = models.CharField(max_length=255, null=True)
    contact_3 = models.CharField(max_length=255, null=True)
    address = models.CharField(max_length=255)
    avatar = models.ImageField(upload_to=filepath_avatar, null=True)
    groups = models.ManyToManyField(Group, related_name="roles")
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE, null=True)
