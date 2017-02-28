from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt
from django.core.urlresolvers import reverse
from .models import User, Secret, Like
from django.db.models import Count

# Create your views here.
def log_reg(request):
    request.session['id'] = None #automatically log you out anytime you direct to the login page
    return render(request, 'dojo_secrets/log_reg.html')

def index(request):
    context = {
                'secrets': Secret.objects.annotate(like_count=Count('likes_secrets')).order_by('-created_at')[:5],
                'logged_in_user': User.userManager.get(id=request.session['id']),
                'logged_in_user_liked_secrets': Secret.objects.filter(likes_secrets__user=User.userManager.get(id=request.session['id']))
                }
    return render(request, 'dojo_secrets/index.html', context)

def popular(request):
    context = {
                'secrets': Secret.objects.annotate(like_count=Count('likes_secrets')).order_by('-like_count'),
                'logged_in_user': User.userManager.get(id=request.session['id']),
                'logged_in_user_liked_secrets': Secret.objects.filter(likes_secrets__user=User.userManager.get(id=request.session['id']))
                }
    return render(request, 'dojo_secrets/popular.html', context)

def register(request):
    x = User.userManager.register(request.POST['first_name'], request.POST['last_name'],\
        request.POST['email'], request.POST['password'], request.POST['pass_conf'])
    if x[0] == True:
        User.userManager.create(first_name=x[2], last_name=x[3], email=x[4], \
                password=bcrypt.hashpw(x[5].encode(), bcrypt.gensalt()))
        request.session['id'] = User.userManager.get(email=x[4]).id
        return redirect(reverse('index'))
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
        return redirect(reverse('log_reg'))

def login(request):
    x = User.userManager.login(request.POST['email'], request.POST['password'])
    if x[0] == True:
        request.session['id'] = User.userManager.get(email=x[1]).id
        return redirect(reverse('index'))
    else:
        messages.error(request, x[1], extra_tags='login')
        return redirect(reverse('log_reg'))

def secret(request):
    Secret.objects.create(secret=request.POST['secret'], user=User.userManager.get(id=request.session['id']))
    return redirect(reverse('index'))

def like(request):
    Like.objects.create(secret=Secret.objects.get(id=request.POST['liked_secret']), user=User.userManager.get(id=request.session['id']))
    return redirect(reverse('index'))

def delete(request):
    Secret.objects.get(id=request.POST['deleting_secret']).delete()
    return redirect(reverse('index'))
