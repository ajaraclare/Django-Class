from django.shortcuts import render

from django . http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("This is the Homepage")

def contact (request):
    return HttpResponse("This is the Contact Page")