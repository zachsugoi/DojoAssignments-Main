from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'disappearing_ninjas/index.html')

def all_ninjas(request):
    return render(request, 'disappearing_ninjas/all_ninjas.html')

def colors(request, color):
    if color == 'red':
        return render(request, 'disappearing_ninjas/red.html')
    elif color == 'blue':
        return render(request, 'disappearing_ninjas/blue.html')
    elif color == 'orange':
        return render(request, 'disappearing_ninjas/orange.html')
    elif color == 'purple':
        return render(request, 'disappearing_ninjas/purple.html')
    else:
        return render(request, 'disappearing_ninjas/april.html')
