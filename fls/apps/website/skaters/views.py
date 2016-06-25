from django.shortcuts import render
from django.http import HttpResponse


def skaters(request):
    context = {
        'active_page' : 'skaters',
    }
    return render(request, 'skaters/index.html', context)

def tables(request):
    context = {
        'active_page' : 'skater_tables',
    }
    return render(request, 'skaters/tables/index.html', context)

