from __future__ import unicode_literals
import re
from django.db import models

class UserManager(models.Manager):
    def register(self, email):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(email):
            return (False, 'Invalid email format')
        else:
            return (True, email)

# Create your models here.
class Email(models.Model):
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    userManager = UserManager()
