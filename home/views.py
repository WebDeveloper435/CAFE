from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    context={
        "variable1":"this is cafe",
        "variable2":"this is point",
    }
    return render(request,"index.html",context)
 
def about(request):
   return render(request,"about.html")

def menu(request):
   return render(request,"menu.html")

def contact(request):
   return render(request,"contact.html")
      
  
   