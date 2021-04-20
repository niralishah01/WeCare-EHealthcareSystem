from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from registration.models import SearchDiseaseResult, SearchSymptomRecord
from django.core import serializers
from django.template.context_processors import csrf
from django.template.loader import render_to_string
import csv
import datetime
from weasyprint import HTML
import tempfile
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
    dataset=SearchSymptomRecord.objects.all().order_by('-searchcount')
    data=[]
    labels=[]
    count=0
    for d in dataset:
        labels.append(d.symptom)
        data.append(d.searchcount) 
        count=count+1
        if count==5:
            break
    print(labels)
    print(data)       
    return render(request,'dashboard1.html',{'tabledata':dataset,'label':labels,'data':data})

def dashboard2(request):
    dataset=SearchDiseaseResult.objects.all().order_by('-searchcount')
    data=[]
    labels=[]
    for d in dataset:
        labels.append(d.diseasename.name)
        data.append(d.searchcount) 
    print(labels)
    print(data)       
    return render(request,'dashboard2.html',{'tabledata':dataset,'label':labels,'data':data})

def pivot_data(request):
    dataset=SearchSymptomRecord.objects.all()
    # data={}
    # for d in dataset:
    #     data[d]=d
    data={}
    for d in dataset:
        data[d.symptom]=d.searchcount

    # data=serializers.serialize('json',dataset)
    print(data)
    return JsonResponse({'symptomrecord':data},safe=False)

def pivot_data2(request):
    dataset=SearchDiseaseResult.objects.all()
    data2=serializers.serialize('json',dataset)
    return JsonResponse(data2,safe=False)

def export_csv(request):
    response=HttpResponse(content_type='text/csv')
    response['Content-Disposition']='attachment; filename=Records'+  str(datetime.datetime.now())+'.csv'
    writer=csv.writer(response)
    writer.writerow(['Symptom','no of searches'])
    record=SearchSymptomRecord.objects.all().order_by('-searchcount')

    for r in record:
        writer.writerow([r.symptom,r.searchcount])
    return response

def export_csv2(request):
    response=HttpResponse(content_type='text/csv')
    response['Content-Disposition']='attachment; filename=DiseaseRecords'+  str(datetime.datetime.now())+'.csv'
    writer=csv.writer(response)
    writer.writerow(['Symptom','no of searches'])
    record=SearchDiseaseResult.objects.all().order_by('-searchcount')

    for r in record:
        writer.writerow([r.diseasename.name,r.searchcount])
    return response

def export_pdf(request):
    response=HttpResponse(content_type='application/pdf')
    response['Content-Disposition']='attachment; filename=Records'+  str(datetime.datetime.now())+'.pdf'
    
    response['Content-Transfer-Encoding']='binary'
    # record=SearchSymptomRecord.objects.all().order_by('-searchcount')

    html_string=render_to_string('pdfoutput.html',{'records':[]})
    html=HTML(string=html_string)
    result=html.write_pdf()

    with tempfile.NamedTemporaryFile(delete=True) as output:
        output.write(result)
        output.flush()
        
        output=open(output.name,'rb')
        response.write(output.read())

    return response
    
