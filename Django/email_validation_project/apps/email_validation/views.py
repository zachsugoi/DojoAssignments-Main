from django.shortcuts import render, redirect
from django.db.models import Max
from .models import Email
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'email_validation/index.html')

def submission(request):
    x = Email.userManager.register(request.POST['email'])
    if x[0] == True:
        Email.userManager.create(email=x[1])
        added_email_id = Email.userManager.all().aggregate(Max('id'))['id__max']
        context = {
                    'added_email': Email.userManager.get(id=added_email_id),
                    'emails': Email.userManager.all()
                }
        return render(request, 'email_validation/success.html', context)
    else:
        messages.error(request, x[1])
        return redirect('/')
