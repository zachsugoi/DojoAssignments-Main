from django.shortcuts import render, redirect
from .models import Course
from ..login_registration.models import User
from django.core.urlresolvers import reverse
from django.db.models import Count

# Create your views here.
def index(request):
    context = {
                'courses': Course.objects.all()
                }
    return render(request, 'courses/index.html', context)

def add(request):
    Course.objects.create(name=request.POST['name'], description=request.POST['description'])
    return redirect(reverse('courses:index'))

def destroy(request, id):
    context = {
                'course_id': id,
                'course': Course.objects.get(id=id)
                }
    return render(request, 'courses/destroy.html', context)

def delete(request):
    Course.objects.get(id=request.POST['course_id']).delete()
    return redirect('/')

def users_courses(request):
    context = {
                'courses': Course.objects.annotate(user_count=Count('user')),
                'users': User.userManager.all()
                }
    return render(request, 'courses/users_courses.html', context)

def add_user(request):
    x = Course.objects.get(name=request.POST['course'])
    add_user = User.userManager.get(id=request.POST['user']) #might have to do a get to pull the whole user object here!
    x.user = add_user
    x.save()
    return redirect(reverse('courses:users_courses'))
