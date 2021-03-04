from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template.context_processors import csrf
from django.db.models import Q
from registration.models import Hospital


# Create your views here.
def gethospitalinfo(request):
    c={}
    c.update(csrf(request))
    return render(request,'addhospitalinfo.html',c)

def addhospitalinfo(request):
    hospital_name=request.POST.get('hospital_name','')
    hospital_address=request.POST.get('hospital_address','')
    hospital_location=request.POST.get('location','')
    hospital_speciality=request.POST.get('speciality','')
    hospital_timing = request.POST.get('timings','')
    print(hospital_address)
    count=0
    hospital=Hospital.objects.all()
    if hospital is not None:
        for hosp in hospital:
            if hosp.name==hospital_name:
                count=1
                break
    if(count!=1):
        h=Hospital(name=hospital_name,location=hospital_location,speciality=hospital_speciality,timings=hospital_timing,address=hospital_address)
        h.save()
        return HttpResponseRedirect('/home/adminhome')
    else:
        return render(request,'addhospitalinfo.html',{'msg1':'Information for this hospital is already added, you can update it later....'})

def gethospital(request):
    query=request.GET['hospital']
    submitbutton= request.GET['search']
    print(query)
    if query!='':
        lookups=Q(name__icontains=query)
        print(lookups)
        object_list=Hospital.objects.filter(lookups)
        print(object_list)
        if (object_list):
            return render(request,'hospitalsearchresults.html',{'objectlist':object_list,'found':True})
        else:
            return render(request,'hospitalsearchresults.html',{'errmsg':"SORRY: No search result found...."})
    else:
        return render(request,'hospitalsearchresults.html',{'errmsg':"Enter appropriate search value"})

def viewhospital(request):
    hosp=Hospital.objects.all()
    return render(request,'viewhospital.html',{'hosp':hosp})

def getupdatedhospitalinfo(request):
    hname=request.GET.get('hname','')
    print(hname)
    hosp=Hospital.objects.get(name=hname)
    c={}
    c.update(csrf(request))
    return render(request,'updatehospitalinfo.html',{'hosp':hosp,'c':c})

def updatehospitalinfo(request):
    hospital_name=request.POST.get('hospital_name','')
    hospital_address=request.POST.get('hospital_address','')
    hospital_location=request.POST.get('location','')
    hospital_speciality=request.POST.get('speciality','')
    hospital_timing = request.POST.get('timings','')
    print(hospital_address)
    Hospital.objects.filter(name=hospital_name).update(address=hospital_address,location=hospital_location, speciality=hospital_speciality,timings=hospital_timing)
    return HttpResponseRedirect('/hospital/viewhospital')

def deletehospital(request):
    hospital_name=request.GET.get('hname','')
    d= Hospital.objects.get(name=hospital_name)
    d.delete()
    return HttpResponseRedirect('/hospital/viewhospital')
