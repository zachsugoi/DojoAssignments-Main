import datetime
from django.shortcuts import render

# Create your views here.
def index(request):
    time = {
            'curr_time': datetime.datetime.now()
    }
    return render(request, 'timedisplay/index.html', time)
