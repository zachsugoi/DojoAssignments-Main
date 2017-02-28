from django.shortcuts import render, redirect
import random, string
# Create your views here.
def index(request):
    if not 'attempt' in request.session:
        request.session['attempt'] = 0
    return render(request, 'random_word_generator/index.html')

def rand_word(request):
    request.session['attempt'] += 1
    x = ''
    for count in range(14):
    	x += random.choice(string.ascii_uppercase)
    request.session['random_word'] = x
    return redirect('/')
