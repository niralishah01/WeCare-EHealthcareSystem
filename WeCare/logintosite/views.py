from django.shortcuts import render
from django.template.context_processors import csrf
from django.http import HttpResponseRedirect
from registration.models import UserDetails
# Create your views here.
def login(request):
    l={}
    l.update(csrf(request))
    return render(request,'login.html',l)

def authentication(request):
    uname=request.POST['email']
    password=request.POST['password']
    users=UserDetails.objects.all()
    for user in users:
        if user.emailID==uname:
            if user.password==password:
                count=1
                break
            else:
                count=0
                break
        else:
            count=-1
    if count==-1:
        return render(request,'login.html',{'msg':'user does not exist'})
    elif count==0:
        return render(request,'login.html',{'msg':'invalid password'})
    else:
        if(user.IsAdmin):
            return HttpResponseRedirect('home/adminhome/')
        elif(user.IsDoctor):
            return HttpResponseRedirect('home/doctorhome/')
    