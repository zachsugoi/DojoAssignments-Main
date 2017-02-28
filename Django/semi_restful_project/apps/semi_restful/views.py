from django.shortcuts import render, redirect
from .models import Product
from django.core.urlresolvers import reverse
# Create your views here.
def index(request):
    context = {
                'products': Product.objects.all()
                }
    return render(request, 'semi_restful/index.html', context)

def new(request):
    return render(request, 'semi_restful/new.html')

def create(request):
    Product.objects.create(name=request.POST['name'], description=request.POST['description'], price=request.POST['price'])
    return redirect(reverse('products:index'))

def destroy(request, id):
    Product.objects.get(id=id).delete()
    return redirect(reverse('products:index'))

def show(request, id):
    context = {
                'product': Product.objects.get(id=id)
                }
    return render(request, 'semi_restful/show.html', context)

def edit(request, id):
    context = {
                'product': Product.objects.get(id=id)
                }
    return render(request, 'semi_restful/edit.html', context)

def update(request, id):
    to_update = Product.objects.get(id=id)
    to_update.name = request.POST['name']
    to_update.description = request.POST['description']
    to_update.price = request.POST['price']
    to_update.save()
    return redirect(reverse('products:index'))
