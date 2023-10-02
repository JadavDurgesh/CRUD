from django.shortcuts import render,redirect
from .models import*
from .serializers import Studentserializers
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer


# Create your views here. 


def Student_all(request):
    sall = Student.objects.all()
    serializersData = Studentserializers(sall,many=True)

    Json_data = JSONRenderer().render(serializersData.data)
    return HttpResponse(Json_data,content_type="application/json")



def add(request):
    if request.POST:
        name = request.POST['name']
        subject = request.POST['subject']
        city = request.POST['city']
        email = request.POST['email']
        password = request.POST['password']
        

        uid = Student.objects.create(name = name,
                                    subject=subject,
                                    city=city,
                                    email=email,
                                    password=password)
        
        return redirect('read')
    
    else:
        
        return render(request,"api/add.html")


def read(request):
    uid = Student.objects.all()
    
    context = {
        'uid' : uid
    }
    return render(request,"api/read.html",context)

def deletes(request,id):
    uid = Student.objects.get(id=id)
    uid.delete()
    return redirect('read')
 
        
def updates(request,id):
    uid = Student.objects.get(id=id)
    if request.POST:
        email = request.POST['email']
        password = request.POST['password']
        name = request.POST['name']
        subject = request.POST['subject']
        city = request.POST['city']
        
        
        uid.email = email
        uid.password = password
        uid.name = name
        uid.subject = subject
        uid.city = city
        uid.save()
        
        
        return redirect('read')
    else:
        return render(request,'api/read.html')


        











