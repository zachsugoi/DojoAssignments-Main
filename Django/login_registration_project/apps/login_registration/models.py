from __future__ import unicode_literals

from django.db import models
import re, bcrypt

# Create your models here.
class UserManager(models.Manager):
    def register(self, first_name, last_name, email, password, pass_conf):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-0._-]+\.[a-zA-Z]+$')
        validation = [] #this will have the Trues and Falses
        flash_errors = {'first_name': [],
                        'last_name': [],
                        'email': [],
                        'password': [],
                        'pass_conf': []
                        }
        #first name
        if len(first_name) < 2:
            validation.append(False)
            flash_errors['first_name'].append('First name required')
        else:
            validation.append(True)
        if not first_name.isalpha() and len(first_name) >= 2:
            flash_errors['first_name'].append('First name can be letters only')
        else:
            validation.append(True)
        #last name
        if len(last_name) < 2:
            validation.append(False)
            flash_errors['last_name'].append('Last name required')
        else:
            validation.append(True)
        if not last_name.isalpha() and len(last_name) >= 2:
            flash_errors['last_name'].append('Last name can be letters only')
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
        print('*'*50)
        print User.userManager.filter(email=email)
        print('*'*50)
        if User.userManager.filter(email=email).count() > 0:
            validation.append(False)
            flash_errors['email'].append('Email already registered')
        else:
            validation.append(True)
        #password
        if len(password) < 8:
            validation.append(False)
            flash_errors['password'].append('Password requires at least 8 characters')
        else:
            validation.append(True)
        #pass conf
        if pass_conf != password:
            validation.append(False)
            flash_errors['pass_conf'].append('Password and Password confirmation do not match')
        else:
            validation.append(True)
        success = all(validation)
        return (success, flash_errors, first_name, last_name, email, password)
    def login(self, email, password):
        if User.userManager.filter(email=email).count() > 0:
            if bcrypt.hashpw(password.encode(), User.userManager.get(email=email).password.encode()) == User.userManager.get(email=email).password.encode():
                return (True, email)
            else:
                return (False, 'Password is incorrect for supplied email address')
        else:
            return (False, 'Supplied email is unregistered')

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    userManager = UserManager()
