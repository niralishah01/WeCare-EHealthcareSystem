from django.http import HttpResponseRedirect
from django.template.context_processors import csrf
from django.shortcuts import render
from django.db.models import Q
from registration.models import Disease

# # Create your views here.
def getdiseaseinfo(request):
    c={}
    c.update(csrf(request))
    return render(request,'adddiseaseinfo.html',c)

def adddiseaseinfo(request):
    disease_name=request.POST['disease_name']
    disease_symptoms=request.POST['symptoms']
    disease_cause=request.POST['cause']
    desc=request.POST['description']
    count=0
    diseases=Disease.objects.all()
    if diseases is not None:
        for dis in diseases:
            if dis.name==disease_name:
                count=1
                break
    if(count!=1):
        d=Disease(name=disease_name,Symptoms=disease_symptoms,Description=desc,Cause=disease_cause)
        d.save()
        return HttpResponseRedirect('/home/doctorhome')
    else:
        return render(request,'adddiseaseinfo.html',{'msg1':'Inforation for this Disease is already added, you can update it later....'})

def getsearchresults(request):
    query=request.GET['q']
    submitbutton= request.GET['search']
    print(query)
    if query!='':
        lookups=Q(name__icontains=query)
        #print(lookups)
        object_list=Disease.objects.filter(lookups)
        #print(object_list)
        if (object_list):
            return render(request,'searchresults.html',{'objectlist':object_list,'found':True})
        else:
            return render(request,'searchresults.html',{'errmsg':"SORRY: No search result found...."})
    else:
        return render(request,'searchresults.html',{'errmsg':"Enter appropriate search value"})
def viewdiseases(request):
    f=request.GET['found']
    print(f)
    diseases=Disease.objects.all()
    if(f==True):
        return render(request,'viewdiseases.html',{'diseases':diseases,'found':f})
    else:
         return render(request,'viewdiseases.html',{'diseases':diseases,'notfound':f})

def getupdateinfo(request):
    dname=request.GET['dname']
    print(dname)
    dis=Disease.objects.filter(name=dname)
    c={}
    c.update(csrf(request))
    return render(request,'updatediseaseinfo.html',{'dis':dis,'c':c})

def updatediseaseinfo(request):
    disease_name=request.POST['disease_name']
    disease_symptoms=request.POST['symptoms']
    disease_cause=request.POST['cause']
    desc=request.POST['description']

    Disease.objects.filter(name=disease_name).update(Symptoms=disease_symptoms,Cause=disease_cause,Description=desc)
    return HttpResponseRedirect('/Diseases/viewdiseases/?found=True')

def deletedisease(request):
    disease_name=request.GET['dname']
    d= Disease.objects.get(name=disease_name)
    d.delete()