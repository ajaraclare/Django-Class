from django.shortcuts import render,HttpResponse

# Create your views here.
def practise (request):
     return HttpResponse("This is my own django project")

def contact (request):
     return HttpResponse("This is the Contact Page")