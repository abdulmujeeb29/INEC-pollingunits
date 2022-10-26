from django.shortcuts import render
from pollingapp.models import *

# Create your views here.

def display(request):
    Pollingunit = Pollingunit.objects.all()
    return render(request,'display.html',{Pollingunit: 'Pollingunit'})


def result(request):
    sum_pollingunit = 0
    if Lga.objects.filter(name=Pollingunit).exists():
        sum_pollingunit = sum(Pollingunit)


    return render(request,'result.html',{ sum_pollingunit :'sum_pollingunit'})


def party(request):
    party= Party.objects.all()
    return render(request,'party.html',{party : 'party '})





