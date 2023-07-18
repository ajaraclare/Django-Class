from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')

def insertdata(request):
    return render(request, 'index.html')