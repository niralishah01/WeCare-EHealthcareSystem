from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template.context_processors import csrf
from django.db.models import Q
from registration.models import Pharmacy
# Create your views here.
def getpharmacyinfo(request):
    c={}
    c.update(csrf(request))
    return render(request,'addpharmacyinfo.html',c)

def addpharmacyinfo(request):
    pharmacy_name=request.POST['pharmacy_name']
    pharmacy_location=request.POST['location']
    count=0
    pharmacy=Pharmacy.objects.all()
    if pharmacy is not None:
        for pharm in pharmacy:
            if pharm.name==pharmacy_name:
                count=1
                break
    if(count!=1):
        p=Pharmacy(name=pharmacy_name,location=pharmacy_location)
        p.save()
        return HttpResponseRedirect('/home/adminhome')
    else:
        return render(request,'addpharmacyinfo.html',{'msg1':'Information already added, you can update it later....'})

def getpharmacy(request):
    query=request.GET.get('pharmacy','')
    #submitbutton= request.GET['search']
    print(query)
    if query!='':
        lookups=Q(name__icontains=query)
        object_list=Pharmacy.objects.filter(lookups)
        print(object_list)
        if (object_list):
            return render(request,'pharmacysearchresults.html',{'objectlist':object_list,'found':True})
        else:
            return render(request,'pharmacysearchresults.html',{'errmsg':"SORRY: No search result found...."})
    else:
        return render(request,'pharmacysearchresults.html',{'errmsg':"Enter appropriate search value"})


def viewpharmacy(request):
    pharm=Pharmacy.objects.all()
    return render(request,'viewpharmacy.html',{'pharm':pharm})

def getupdatedpharmacyinfo(request):
    pname=request.POST.get('pharmacy_name','')
    print(pname)
    pharm=Pharmacy.objects.filter(name=pname)
    c={}
    c.update(csrf(request))
    print("in updated")
    return render(request,'updatepharmacyinfo.html',{'pharm':pharm,'c':c})

def updatepharmacyinfo(request):
    print("update")
    pharmacy_name=request.POST.get('pharmacy_name','')
    pharmacy_location=request.POST.get('location','')
    Pharmacy.objects.filter(name=pharmacy_name).update(location=pharmacy_location)
    return HttpResponseRedirect('/pharamacy/viewpharmacy')

def deletepharmacy(request):
    pharmacy_name=request.GET.get('pname','')
    d= Pharmacy.objects.get(name=pharmacy_name)
    d.delete()
    return HttpResponseRedirect('/pharamacy/viewpharmacy')