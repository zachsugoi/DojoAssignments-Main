from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt
from django.core.urlresolvers import reverse
from .models import User, Product, Wish

# Create your views here.
def index(request):
    return render(request, 'wishlist/index.html')

def register(request):
    x = User.userManager.register(request.POST['name'], request.POST['username'],\
        request.POST['password'], request.POST['pass_conf'], request.POST['hire_date'])
    if x[0] == True:
        User.userManager.create(name=x[2], username=x[3],\
                password=bcrypt.hashpw(x[4].encode(), bcrypt.gensalt()), \
                hire_date=x[5])
        request.session['id'] = User.userManager.get(username=x[3]).id
        return redirect(reverse('dashboard'))
    else:
        for flash in x[1]['name']:
            messages.error(request, flash, extra_tags='name')
        for flash in x[1]['username']:
            messages.error(request, flash, extra_tags='username')
        for flash in x[1]['password']:
            messages.error(request, flash, extra_tags='password')
        for flash in x[1]['pass_conf']:
            messages.error(request, flash, extra_tags='pass_conf')
        for flash in x[1]['hire_date']:
            messages.error(request, flash, extra_tags='hire_date')
        return redirect(reverse('index'))

def login(request):
    x = User.userManager.login(request.POST['username'], request.POST['password'])
    if x[0] == True:
        request.session['id'] = User.userManager.get(username=x[1]).id
        return redirect(reverse('dashboard'))
    else:
        messages.error(request, x[1], extra_tags='login')
        return redirect(reverse('index'))

def dashboard(request):
    context = {
                'logged_in_user': User.userManager.get(id=request.session['id']),
                'logged_user_wished_products': Product.productManager.filter(wished_products__user=User.userManager.get(id=request.session['id'])),
                'other_user_wished_products': Product.productManager.exclude(wished_products__user=User.userManager.get(id=request.session['id']))
                }
    return render(request, 'wishlist/dashboard.html', context)

def delete(request, id):
    Product.productManager.get(id=id).delete()
    return redirect(reverse('dashboard'))

def remove(request, id):
    Wish.objects.get(user=User.userManager.get(id=request.session['id']), product=Product.productManager.get(id=id)).delete()
    return redirect(reverse('dashboard'))

def add_wish(request, id):
    Wish.objects.create(product=Product.productManager.get(id=id), user=User.userManager.get(id=request.session['id']))
    return redirect(reverse('dashboard'))

def create(request):
    return render(request, 'wishlist/create.html')

def logout(request):
    request.session['id'] = None
    return redirect(reverse('index'))

def create_product(request):
    x = Product.productManager.item_add(request.POST['product'])
    if x[0] == True:
        Product.productManager.create(product=x[2], user=User.userManager.get(id=request.session['id']))
        Wish.objects.create(product=Product.productManager.get(product=x[2]), user=User.userManager.get(id=request.session['id']))
        return redirect(reverse('dashboard'))
    else:
        for flash in x[1]:
            messages.error(request, flash)
        return redirect(reverse('create'))

def wish_items(request, id):
    context = {
                'product': Product.productManager.get(id=id),
                'liking_users': User.userManager.filter(wishing_user__product=Product.productManager.get(id=id))
            }
    return render(request, 'wishlist/wish_items.html', context)
