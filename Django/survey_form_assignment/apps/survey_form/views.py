from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'survey_form/index.html')

def process(request):
    if len(request.POST['name']) < 1:
        return redirect('/')
    else:
        if not 'count' in request.session:
            request.session['count'] = 1
        else:
            request.session['count'] += 1
        global form_data
        form_data = {
                    'name': request.POST['name'],
                    'location': request.POST['location'],
                    'language': request.POST['language'],
                    'comment': request.POST['comment']
        }
    return redirect('/result')

def result(request):
    return render(request, 'survey_form/result.html', form_data)
