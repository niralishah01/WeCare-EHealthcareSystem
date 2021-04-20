from django.http import HttpResponseRedirect
from django.template.context_processors import csrf
from django.shortcuts import render
from django.db.models import Q
from registration.models import Disease,SkinDisease,DiseaseTreatment,SearchDiseaseResult

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
        return render(request,'adddiseaseinfo.html',{'msg1':'Information for this Disease is already added, you can update it later....'})

def getsearchresults(request):
    query=request.GET['q']
    submitbutton= request.GET['search']
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
    diseases=Disease.objects.all()
    return render(request,'viewdiseases.html',{'diseases':diseases})

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
    return HttpResponseRedirect('/Diseases/viewdiseases/')

def deletedisease(request):
    disease_name=request.GET['dname']
    d= Disease.objects.get(name=disease_name)
    d.delete()
    return HttpResponseRedirect('/Diseases/viewdiseases/')

def homesearch(request):
    query=request.GET.get('q','')
    print(query)
    if query!='':
        lookups=Q(name__icontains=query)
        print(lookups)
        object_list=Disease.objects.filter(lookups)
        print(object_list)
        if (object_list):
            for o in object_list:
                d1=SearchDiseaseResult.objects.filter(diseasename=o)
                if(not d1):
                    d1=SearchDiseaseResult(diseasename=o,searchcount=1)
                    d1.save()
                else:
                    d1=SearchDiseaseResult.objects.get(diseasename=o)
                    d1.searchcount=d1.searchcount+1
                    d1.save()
            return render(request,'homesearchresult.html',{'objectlist':object_list,'found':True})
        else:
            return render(request,'homesearchresult.html',{'errmsg':"SORRY: No search result found...."})
    else:
        return render(request,'homesearchresult.html',{'errmsg':"Enter appropriate search value"})

def getskindiseaseinfo(request):
    c={}
    c.update(csrf(request))
    return render(request,'addskindisease.html',c)

def addskindiseaseinfo(request):
    disease_name=request.POST.get('disease_name','')
    image1 = request.FILES.get('image1','')
    image2 = request.FILES.get('image2','')
    image3 = request.FILES.get('image3','')
    count=0
    diseases=SkinDisease.objects.all()
    if diseases is not None:
        for dis in diseases:
            if dis.name==disease_name:
                count=1
                break
    if(count!=1):
        d=SkinDisease(name=disease_name,image1=image1,image2=image2,image3=image3)
        d.save()
        return HttpResponseRedirect('/home/doctorhome')
    else:
        return render(request,'addskindisease.html',{'msg1':'Information for this Disease is already added, you can update it later....'})

def viewskindiseases(request):
    diseases=SkinDisease.objects.all()
    return render(request,'viewskindiseases.html',{'diseases':diseases})

def searchskindiseasefromimage(request):
    data=SkinDisease.objects.all()
    return render(request,'searchskindiseasefromimage.html',{'diseases':data})

def getdiseasetreatmentinfo(request):
    diseasedata=Disease.objects.all()
    c={}
    c.update(csrf(request))
    return render(request,'adddiseasetreatment.html',{'c':c,'diseasedata':diseasedata})

def adddiseasetreatment(request):
    desc=request.POST['desc']
    dur=request.POST['dur']
    dis=request.POST['disease']
    d=Disease.objects.get(name=dis)
    dts=DiseaseTreatment.objects.all()
    found=False
    for dt in dts:
        if(dt.Disease_id==d):
            found=True
    if(found):
        diseasedata=Disease.objects.all()
        c={}
        c.update(csrf(request))
        return render(request,'adddiseasetreatment.html',{'c':c,'diaseasedata':diseasedata,'msg1':'Treatment is already added for ths disease.. you can add more etails in it later.'})
    dt=DiseaseTreatment(description=desc,duration=dur,Disease_id=d)
    dt.save()
    return HttpResponseRedirect('/home/doctorhome/')

def gettreatmentdetails(request):
    disnm=request.GET['dname']
    dis=Disease.objects.get(name=disnm)
    dst=DiseaseTreatment.objects.filter(Disease_id=dis)
    if(not dst):
        return render(request,'viewupdatediseasetreatmentdetails.html',{'msg':'Treatment for this disease is not available yet,it will be available soon..You cam also ask about this in our FAQ section'})
    dt=DiseaseTreatment.objects.get(Disease_id=dis)
    print(dt.Disease_id.name)
    c={}
    c.update(csrf(request))
    return render(request,'viewupdatediseasetreatmentdetails.html',{'c':c,'dt':dt})

def updatediseasetreatment(request):
    dname=request.POST['dname']
    desc=request.POST['desc']
    dur=request.POST['dur']
    d=Disease.objects.get(name=dname)
    dt=DiseaseTreatment.objects.get(Disease_id=d)
    dt.description=desc
    dt.duration=dur
    dt.save()
    return HttpResponseRedirect('/Diseases/viewdiseases/')

def getsearchresults2(request):
    query=request.GET['q']
    submitbutton= request.GET['search']
    if query!='':
        lookups=Q(name__icontains=query)
        #print(lookups)
        object_list=DiseaseTreatment.objects.filter(lookups)
        if (object_list):
            return render(request,'searchresults2.html',{'objectlist':object_list,'found':True})
        else:
            return render(request,'searchresults2.html',{'errmsg':"SORRY: No search result found...."})
    else:
        return render(request,'searchresults2.html',{'errmsg':"Enter appropriate search value"})