from __future__ import unicode_literals
import re, bcrypt
from django.db import models

# Create your models here.
class UserManager(models.Manager):
    def register(self, first_name, last_name, email, password, pass_conf):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-0._-]+\.[a-zA-Z]+$')
        validation = []
        flash_errors = {'first_name': [],
                        'last_name': [],
                        'email': [],
                        'password': [],
                        'pass_conf': []
                        }
        #first_name
        if len(first_name) < 1:
            validation.append(False)
            flash_errors['first_name'].append('First name required')
        else:
            validation.append(True)
        #last_name
        if len(last_name) < 1:
            validation.append(False)
            flash_errors['last_name'].append('Last name required')
        else:
            validation.append(True)
        #email
        if len(email) < 1:
            validation.append(False)
            flash_errors['email'].append('Email required')
        else:
            validation.append(True)
        if not EMAIL_REGEX.match(email) and len(email) > 0:
            validation.append(False)
            flash_errors['email'].append('Invalid email format')
        else:
            validation.append(True)
        if User.userManager.filter(email=email).count() > 0:
            validation.append(False)
            flash_errors['email'].append('Email already registered')
        else:
            validation.append(True)
        #password
        if len(password) < 8:
            validation.append(False)
            flash_errors['password'].append('Password must be at least 8 characters')
        else:
            validation.append(True)
        #pass_conf
        if password != pass_conf:
            validation.append(False)
            flash_errors['pass_conf'].append('Password and password confirmation do not match')
        else:
            validation.append(True)
        success = all(validation)
        return (success, flash_errors, first_name, last_name, email, password)
    def login(self, email, password):
        if User.userManager.filter(email=email).count() > 0:
            if bcrypt.hashpw(password.encode(), User.userManager.get(email=email).password.encode()) == User.userManager.get(email=email).password.encode():
                return(True, email)
            else:
                return (False, 'Password is incorrect for supplied email address')
        else:
            return (False, 'Email has not been registered')

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    userManager = UserManager()

class Secret(models.Model):
    secret = models.TextField()
    user = models.ForeignKey(User, related_name='secrets')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Like(models.Model):
    secret = models.ForeignKey(Secret, related_name='likes_secrets')
    user = models.ForeignKey(User, related_name='likes_users')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
