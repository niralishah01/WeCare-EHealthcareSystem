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
            data=True
        except:
            data=False
    return render(request,'details.html',{'result':summary,'countrydata':countrydata})