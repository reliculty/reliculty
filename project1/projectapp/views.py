from django.http import HttpResponse
from django.shortcuts import render
from . models import *

# Create your views here.


def demo(request):
    obj1 = Table1.objects.all()
    obj2 = Team.objects.all()
    return render(request, 'index.html', {'res': obj1, 'team': obj2})
