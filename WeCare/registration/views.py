from django.http import HttpResponseRedirect
from django.template.context_processors import csrf
from django.shortcuts import render
from .models import UserDetails
import re

def getregsdetails(request):
    r = {}
    r.update(csrf(request))
    return render(request,'register.html', r)

def addregsdetails(request):
    name=request.POST.get('name','')
    email=request.POST.get('email','')
    password=request.POST.get('passwd','')
    repassword=request.POST.get('repasswd','')
    passwordregex='[a-zA-Z0-9]{6,12}'
    role=request.POST.get('role','')
    admin=False
    doctor=False
    if(role=="admin"):
        admin=True
    elif(role=="doctor"):
        doctor=True
    count=0
    users=UserDetails.objects.all()
    if users is not None:
        for user in users:
            if user.emailID==email:
                count=1
                break
    if count!=1:
        if len(password)>=6 and len(password)<=12:
            if re.search(passwordregex,password):
                
                if password==repassword:
                    u = UserDetails(name=name,emailID=email,password=password,IsAdmin=admin,IsDoctor=doctor)
                    u.save()
                    
                    i={}
                    i.update(csrf(request))
                    
                    return render(request,'index.html')
                else:
                    return render(request,'register.html',{'msg2':'both password must be matched.'}) 
                    
            else:
                return render(request,'register.html',{'msg4':'password credentials are not matched'})
        else:
            return render(request,'register.html',{'msg1':'password must be between 6 to 15 characters'})
    else:
        return render(request,'register.html',{'msg5':'this user is already registered'})


