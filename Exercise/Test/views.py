from django.shortcuts import render,HttpResponse

# Create your views here.

def home (request):
    return HttpResponse("This is the Home page I have created today")

def about(request):
    return HttpResponse("This is the About Page I have also created today")

def contact(request):
    return HttpResponse("This is the Contact Page of today's practise")