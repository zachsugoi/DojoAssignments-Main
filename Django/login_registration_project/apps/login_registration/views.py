from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
import bcrypt

# Create your views here.
def index(request):
    return render(request, 'login_registration/index.html')

def register(request):
    x = User.userManager.register(request.POST['first_name'], request.POST['last_name'],\
            request.POST['email'], request.POST['password'], request.POST['pass_conf'])
    if x[0] == True:
        User.userManager.create(first_name=x[2], last_name=x[3], email=x[4], password=bcrypt.hashpw(x[5].encode(), bcrypt.gensalt()))
        messages.success(request, 'Successfully registered!')
        context = {'first_name': x[2]}
        return render(request, 'login_registration/success.html', context)
    else:
        for flash in x[1]['first_name']:
            messages.error(request, flash, extra_tags='first_name')
        for flash in x[1]['last_name']:
            messages.error(request, flash, extra_tags='last_name')
        for flash in x[1]['email']:
            messages.error(request, flash, extra_tags='email')
        for flash in x[1]['password']:
            messages.error(request, flash, extra_tags='password')
        for flash in x[1]['pass_conf']:
            messages.error(request, flash, extra_tags='pass_conf')
        return redirect('/')

def login(request):
    x = User.userManager.login(request.POST['email'], request.POST['password'])
    if x[0] == True:
        context = {'first_name': User.userManager.get(email=x[1]).first_name}
        messages.success(request, 'Successfully logged in!')
        return render(request, 'login_registration/success.html', context)
    else:
        messages.error(request, x[1], extra_tags='login')
        return redirect('/')
