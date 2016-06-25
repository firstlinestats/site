from django.shortcuts import render
from django.http import HttpResponse


def goalies(request):
    context = {
        'active_page' : 'goalies',
    }
    return render(request, 'goalies/index.html', context)

def tables(request):
    context = {
        'active_page' : 'goalie_tables',
    }
    return render(request, 'goalies/tables/index.html', context)