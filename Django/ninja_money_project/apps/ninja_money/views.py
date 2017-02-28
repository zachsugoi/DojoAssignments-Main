from django.shortcuts import render, redirect
import random, datetime

# Create your views here.
def index(request):
    if not 'total_gold' in request.session:
        request.session['total_gold'] = 0
    if not 'activities' in request.session:
        request.session['activities'] = ''
    #else:
        #Markup(request.session['activities'])
    return render(request, 'ninja_money/index.html')

def process(request, building):
    if building == 'farm':
        increase = random.randrange(10,21)
        request.session['total_gold'] += increase
        request.session['activities'] += "<p class='earn'>Earned "+str(increase)+" golds from the farm! "+datetime.datetime.now().strftime('(%Y/%m/%d %I:%M %p)')+"</p>"
    elif building == 'cave':
        increase = random.randrange(5,11)
        request.session['total_gold'] += increase
        request.session['activities'] += "<p class='earn'>Earned "+str(increase)+" golds from the cave! "+datetime.datetime.now().strftime('(%Y/%m/%d %I:%M %p)')+"</p>"
    elif building == 'house':
        increase = random.randrange(2,6)
        request.session['total_gold'] += increase
        request.session['activities'] += "<p class='earn'>Earned "+str(increase)+" golds from the house! "+datetime.datetime.now().strftime('(%Y/%m/%d %I:%M %p)')+"</p>"
    elif building == 'casino':
        increase = random.randrange(-50,51)
        request.session['total_gold'] += increase
        if increase < 0:
            request.session['activities'] += "<p class='lose'>Entered a casino and lost "+str(abs(increase))+" golds... Ouch.. "+datetime.datetime.now().strftime('(%Y/%m/%d %I:%M %p)')+"</p>"
        else:
            request.session['activities'] += "<p class='earn'>Earned "+str(increase)+" golds from the casino! "+datetime.datetime.now().strftime('(%Y/%m/%d %I:%M %p)')+"</p>"
    return redirect('/')
