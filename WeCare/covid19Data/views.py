from django.shortcuts import render
import requests
# Create your views here.
def getcoronaupdates(request):
    data=False
    while(not data):
        try:
            result=requests.get("https://api.covid19api.com/summary")
            summary=result.json()['Global']
            countrydata=result.json()['Countries']
            # labels=['New Confirmed','Total Confirmed','New Recovered','Total Recovered','New Deaths','Total Deaths']
            # dataset=[summary.NewConfirmed,summary.TotalConfirmed,summary.NewRecovered,summary.TotalRecovered,summary.NewDeaths,summary.TotalDeaths]
            data=True
        except:
            data=False
    # return render(request,'details.html',{'result':summary,'countrydata':countrydata,'labels':labels,'dataset':dataset})
    return render(request,'details.html',{'result':summary,'countrydata':countrydata})