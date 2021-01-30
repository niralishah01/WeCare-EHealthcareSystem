from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template.context_processors import csrf
import requests
import covid
# Create your views here.
def getcoronaupdates(request):
    data=False
    while(not data):
        try:
            result=requests.get("https://api.covid19api.com/summary")
            summary=result.json()['Global']
            # countrydata=result.json()['Countries']
            labels=['New Confirmed','Total Confirmed','New Recovered','Total Recovered','New Deaths','Total Deaths']
            dataset=[summary.NewConfirmed,summary.TotalConfirmed,summary.NewRecovered,summary.TotalRecovered,summary.NewDeaths,summary.TotalDeaths]
            print(dataset)
            data=True
        except:
            data=False
    # return render(request,'details.html',{'result':summary,'countrydata':countrydata,'labels':labels,'data':dataset})
    # return render(request,'details.html',{'result':summary,'countrydata':countrydata})
    # return render(request,'details.html',{'result':summary})
    return render(request,'details.html',{'result':summary,'labels':labels,'data':dataset})

def getoption(request):
    cov=covid.Covid()
    o={}
    o.update(csrf(request))
    # print(cov.get_data())
    actives=cov.get_total_active_cases()
    confirmed=cov.get_total_confirmed_cases()
    recovered=cov.get_total_recovered()
    deaths=cov.get_total_deaths()
    return render(request,'updates.html',{'o':o,'active':actives,'confirmed':confirmed,'recovered':recovered,'deaths':deaths})

def selectoption(request):
    op=request.POST['sel']
    if(op=="GetAllCountryData"):
        return HttpResponseRedirect("/covid19Data/allcountrydata/")
    elif(op=="SelectCountry"):
        return HttpResponseRedirect("/covid19Data/getname/")

def allcountrydata(request):
    cov=covid.Covid()
    actives=cov.get_total_active_cases()
    confirmed=cov.get_total_confirmed_cases()
    recovered=cov.get_total_recovered()
    deaths=cov.get_total_deaths()
    countries = cov.list_countries()
    cname=[]
    cactive=[]
    cconfirmed=[]
    crecovered=[]
    cdeaths=[]
    index=0
    for c in countries:
        t=c['name']
        data=cov.get_status_by_country_name(t)
        cname.append(data['country'])
        cactive.append(data['active'])
        cdeaths.append(data['deaths'])
        crecovered.append(data['recovered'])
        cconfirmed.append(data['confirmed'])
        index+=1
        if(index==25):
            break
    mylist=zip(cname,cactive,cdeaths,crecovered,cconfirmed)
    return render(request,'updates.html',{'active':actives,'confirmed':confirmed,'recovered':recovered,'deaths':deaths,'mylist':mylist})

def getname(request):
    cov=covid.Covid()
    c={}
    c.update(csrf(request))
    actives=cov.get_total_active_cases()
    confirmed=cov.get_total_confirmed_cases()
    recovered=cov.get_total_recovered()
    deaths=cov.get_total_deaths()
    return render(request,'updates.html',{'c':c,'active':actives,'confirmed':confirmed,'recovered':recovered,'deaths':deaths})

def coronaDetails(request):
    cov=covid.Covid()
    name=request.POST['countryname']
    print(name)
    actives=cov.get_total_active_cases()
    confirmed=cov.get_total_confirmed_cases()
    recovered=cov.get_total_recovered()
    deaths=cov.get_total_deaths()
   
    virusdata=cov.get_status_by_country_name(name)
    active=virusdata['active']
    recover=virusdata['recovered']
    deaths=virusdata['deaths']
    label=["Active","Recovered","Deaths"]
    data=[active,recover,deaths]
    return render(request,'updates.html',{'label':label,'data':data,'name':name,'active':actives,'confirmed':confirmed,'recovered':recovered,'deaths':deaths})

