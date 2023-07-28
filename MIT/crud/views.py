from django.shortcuts import render, redirect

from . models import Students

# Create your views here.
def home(request):
    # d = Students.objects.all()


    return render(request, 'index.html' )


def students(request):
    d = Students.objects.all()

    return render(request, 'students.html', {"d": d})


def insertdata(request):
    if request.method =="POST":
        name = request.POST.get('name')
        school = request.POST.get('school')
        email = request.POST.get('email')

        data = Students(name=name, school=school, email=email)
        data.save()

        return redirect('/crud/students/')

        # print(name,school,email)

    return render(request, 'index.html')

def delete(request,id):
    dd = Students.objects.get(id=id)
    dd.delete()

    return redirect('/crud')

    return render (request, 'index.html')

def editdata(request,id):
    if request.method == "POST":
        name = request.POST['name']
        school = request.POST['school']
        email = request.POST['email']

        edit = Students.objects.get(id=id)

        edit.name = name
        edit.school = school
        edit.email = email

        edit.save()

        return redirect('/crud')

    ddd = Students.objects.get(id=id)

    context = {"ddd": ddd}

    return render(request, 'edit.html', context)
