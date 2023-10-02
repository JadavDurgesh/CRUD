from django.shortcuts import render,redirect
from .models import *

# Create your views here.

# def crud(request):
#     return render(request,'myapp/crud.html')

def create_user(request):
    if request.POST:
        name=request.POST['name']
        email=request.POST['email']
        eddress=request.POST['eddress']
        phone=request.POST['phone']

        User.objects.create(name=name,
                            email=email,
                            eddress=eddress,
                            phone=phone)
                            
        return redirect('read_user')

    else:
        return render(request,'myapp/crud.html')

def read_user(request):
    uid=User.objects.all()

    contaxt={
        'uid':uid
    }        
    
    return render(request,'myapp/crud.html',contaxt)

def update_user(request,id):
    uid=User.objects.get(id=id)

    if request.POST:
        name=request.POST['name']
        email=request.POST['email']
        eddress=request.POST['eddress']
        phone=request.POST['phone']

        uid.name=name
        uid.email=email
        uid.eddress=eddress
        uid.phone=phone
        uid.save()
         
        return redirect('read_user')
    
    else:

        return redirect('read_user')

def delete_user(request,id):
        uid=User.objects.get(id=id)
        uid.delete()

        return redirect('read_user')
      
    