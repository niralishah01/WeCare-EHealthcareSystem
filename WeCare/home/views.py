from django.shortcuts import render
from django.http import HttpResponsePermanentRedirect
from django.urls import reverse
# Create your views here.
def index(request):
    return render(request,'index.html')
    #return HttpResponsePermanentRedirect(reverse('homepage'))

def doctorhome(request):
    return render(request,'doctor_home.html')

def adminhome(request):
    return render(request,'admin_home.html')