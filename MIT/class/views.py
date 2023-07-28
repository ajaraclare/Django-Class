from django.shortcuts import render

from django . http import HttpResponse

# Create your views here.

def home(request):
    return render(request,'home.html', {'navbar' : 'home'})

def contact (request):
    return render(request,'contact/Contact.html', {'navbar' : 'contact'})

def services (request):
    return render(request,'services.html')