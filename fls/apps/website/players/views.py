from django.shortcuts import render
from django.http import HttpResponse


def skaters(request):
    context = {
        'active_page' : 'skaters',
    }
    return render(request, 'players/skaters/index.html', context)

def goalies(request):
    context = {
        'active_page' : 'goalies',
    }
    return render(request, 'players/goalies/index.html', context)
