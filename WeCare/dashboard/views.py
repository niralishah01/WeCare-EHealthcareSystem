from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from registration.models import SearchDiseaseResult, SearchSymptomRecord
from django.core import serializers
from django.template.context_processors import csrf

# Create your views here.
def gotodashboard(request):
    return render(request,'viewstatistics.html')
def selectoption(request):
    op=request.POST['sel']
    if(op=="SymptomsRecord"):
        return HttpResponseRedirect('/dashboard/dashboard1/')
    elif(op=="DiseaseSearchResults"):
        return HttpResponseRedirect('/dashboard/dashboard2/')

def dashboard1(request):
    return render(request,'dashboard1.html',{})

def dashboard2(request):
    return render(request,'dashboard2.html',{})

def pivot_data(request):
    dataset=SearchSymptomRecord.objects.all()
    data=serializers.serialize('json',dataset)
    return JsonResponse(data,safe=False)

def pivot_data2(request):
    dataset=SearchDiseaseResult.objects.all()
    data2=serializers.serialize('json',dataset)
    return JsonResponse(data2,safe=False)

