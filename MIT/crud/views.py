from django.shortcuts import render

from . models import Students

# Create your views here.
def home(request):
    d = Students.objects.all()


    return render(request, 'index.html', {"d":d} )

def insertdata(request):
    if request.method =="POST":
        name = request.POST.get('name')
        school = request.POST.get('school')
        email = request.POST.get('email')

        data = Students(name=name, school=school, email=email)
        data.save()

        # print(name,school,email)

    return render(request, 'index.html')