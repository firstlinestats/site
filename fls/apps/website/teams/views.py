from django.shortcuts import render
from django.http import HttpResponse


def teams(request):
    context = {
        'active_page' : 'teams',
    }
    return render(request, 'teams/index.html', context)

