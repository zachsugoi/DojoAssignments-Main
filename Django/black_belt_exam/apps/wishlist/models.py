from __future__ import unicode_literals
import bcrypt
from django.db import models

# Create your models here.
class UserManager(models.Manager):
    def register(self, name, username, password, pass_conf, hire_date):
        validation = []
        flash_errors = {'name': [],
                        'username': [],
                        'password': [],
                        'pass_conf': [],
                        'hire_date': [],
                        }
        #name
        if len(name) < 3:
            validation.append(False)
            flash_errors['name'].append('Name must be at least 3 characters')
        else:
            validation.append(True)
        #username
        if len(username) < 3:
            validation.append(False)
            flash_errors['username'].append('Username must be at least 3 characters')
        else:
            validation.append(True)
        if User.userManager.filter(username=username).count() > 0:
            validation.append(False)
            flash_errors['username'].append('Username already registered')
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
        #hire_date
        if not hire_date:
            validation.append(False)
            flash_errors['hire_date'].append('Hire date required')
        else:
            validation.append(True)
        success = all(validation)
        return (success, flash_errors, name, username, password, hire_date)
    def login(self, username, password):
        if User.userManager.filter(username=username).count() > 0:
            if bcrypt.hashpw(password.encode(), User.userManager.get(username=username).password.encode()) == User.userManager.get(username=username).password.encode():
                return(True, username)
            else:
                return (False, 'Password is incorrect for supplied username')
        else:
            return (False, 'Username has not been registered')

class ProductManager(models.Manager):
    def item_add(self, product):
        validation = []
        flash_errors = []
        if len(product) < 3:
            validation.append(False)
            flash_errors.append('Item description must be at least 3 characters')
        else:
            validation.append(True)
        if Product.productManager.filter(product=product).count() > 0:
            validation.append(False)
            flash_errors.append('Product already registered')
        else:
            validation.append(True)
        success = all(validation)
        return (success, flash_errors, product)

class User(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    hire_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    userManager = UserManager()

class Product(models.Model):
    product = models.CharField(max_length=255)
    user = models.ForeignKey(User, related_name='owners')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    productManager = ProductManager()

class Wish(models.Model):
    product = models.ForeignKey(Product, related_name='wished_products')
    user = models.ForeignKey(User, related_name='wishing_user')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
