from django.shortcuts import render
from django.http import HttpResponse


def games(request):
    context = {
        'active_page' : 'games',
    }
    return render(request, 'games/index.html', context)

