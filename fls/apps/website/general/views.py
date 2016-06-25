from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'general/index.html')

def about(request):
    context = {
        'active_page' : 'about'
    }
    return render(request, 'general/about.html', context)

