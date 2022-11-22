from django.shortcuts import render,HttpResponseRedirect
from . forms import StudentForm
from . models import Student
# Create your views here.
def add_show(request):
    if request.method=="POST":
        fm=StudentForm(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data["first_name"]
            lm=fm.cleaned_data["last_name"]
            em=fm.cleaned_data["email"]
            std=Student(first_name=nm,last_name=lm,email=em)
            std.save()

    else:
        fm=StudentForm()
    stud=Student.objects.all()
    return render(request,"app1/add_show.html",{'form':fm,'stud':stud})

def delete(request, id):
    if request.method =="POST":
        di=Student.objects.get(pk=id)
        di.delete()
        return HttpResponseRedirect("/")

def update(request, id):
    if request.method=="POST":
        pi=Student.objects.get(pk=id)
        fm=StudentForm(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
        return HttpResponseRedirect("/")
    else:
        pi=Student.objects.get(pk=id)
        fm=StudentForm(instance=pi)
    return render (request,"app1/show.html",{"form":fm})
