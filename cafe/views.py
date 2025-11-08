
from django.shortcuts import render,HttpResponse

def homepage(request):
    return HttpResponse("welcome to cafe")