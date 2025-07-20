from django.shortcuts import render
# base/views.py

from django.http import HttpResponse
from django.contrib import messages
from base import models
from base.models import Contact
def home(request):
    return render(request,'home.html')
def contact(request):
    if request.method=="POST":
        print('post')
        name=request.POST.get("name")
        email=request.POST.get("email")
        message=request.POST.get("message")
        print(name,email,message)    
        if len(name)>1 and len(name)<30:
           pass
        else:
           messages.error(request,'Length of name should be gretaer than 2 and less than 30 words')
           return  render(request,'home.html')
        
        if len(email)>1 and len(email)<30:
            pass
        else:
            messages.error(request,'Invalid Email Try Again')
            return render(request,'home.html')
        
        ins=models.Contact(name=name,email=email,message=message)
        ins.save()
        messages.success(request,'Thank You for Contacting with me||your message have been saved')
        print('data has been saved to databse')
        print('the request is no pass')
    return render(request,"home.html")    