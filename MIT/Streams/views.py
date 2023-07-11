from django.shortcuts import render , HttpResponse

# Create your views here.

def index(request):
    return render(request, 'home.html')

def blue(request):
    return HttpResponse("This is stream Blue")

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')
