from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context = {
        'name': 'Hung',
        'age': 20,
        'nationality': 'Vietnamese'
    }
    return render(request, 'index.html', context)