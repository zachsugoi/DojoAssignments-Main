from __future__ import unicode_literals
from ..login_registration.models import User
from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=225)
    description = models.CharField(max_length=225)
    user = models.ForeignKey(User, related_name='users', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
