from django.shortcuts import render,redirect
from .models import*
# Create your views here.

def index(request):
    if request.POST:
        name = request.POST['name']
        age = request.POST['age']
        subject = request.POST['subject']

        uid = User.objects.create(name=name,
                                   age=age,
                                   subject=subject)
        return redirect("riad")

    else:
        return render(request, "myapp/index.html")

def riad(request):

    uid = User.objects.all()

    context={
        'uid' : uid
    }
    return render(request, "myapp/riad.html",context)

def deletes(request,id):

    uid = User.objects.get(id=id) 
    uid.delete()
    return redirect('riad')



def updetes(request,id):
    uid = User.objects.get(id=id)
    if request.POST:
        name = request.POST['name']
        age = request.POST['age']
        subject = request.POST['subject']

        uid.name = name
        uid.subject = subject
        uid.save()

        return redirect('riad')

    else:
        return render(request,"myapp/updetes.html")



    