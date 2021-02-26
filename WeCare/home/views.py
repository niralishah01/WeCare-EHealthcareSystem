from django.shortcuts import render
from django.http import HttpResponsePermanentRedirect
from django.urls import reverse
from registration.models import Hospital
from django.db.models import Q
# Create your views here.
def index(request):
    return render(request,'index.html')
    #return HttpResponsePermanentRedirect(reverse('homepage'))

def doctorhome(request):
    return render(request,'doctor_home.html')

def adminhome(request):
    return render(request,'admin_home.html')

def hospitalsearch(request):
    query= request.GET.get('search','')
    print(query)
    if query != '':
        lookups = Q(location__icontains=query)
        object_list=Hospital.objects.filter(lookups)
        if (object_list):
            return render(request,'hospitalsearch.html',{'objectlist':object_list,'found':True})
        else:
            return render(request,'hospitalsearch.html',{'errmsg':"SORRY: No search result found."})
    else:
        return render(request,'hospitalsearch.html',{'errmsg':"Enter appropriate search value"})