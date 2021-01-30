from django.shortcuts import render
from django.http import HttpResponsePermanentRedirect
from django.urls import reverse
import requests
# from newsapi import NewsApiClient
# Create your views here.
def index(request):
    return render(request,'index.html')

def doctorhome(request):
    return render(request,'doctor_home.html')

def adminhome(request):
    return render(request,'admin_home.html')

def news(request):
    # https://www.medicalnewstoday.com/
    # newsapi = NewsApiClient(api_key='81606bad15824906a328e56705cc8f52')
    # top_headlines = newsapi.get_top_headlines(q='bitcoin',
    #                                       sources='bbc-news,the-verge',
    #                                       category='business',
    #                                       language='en',
    #                                       country='us')
    # print(top_headlines)
    # return render(request,'home.html')
    url = ('http://newsapi.org/v2/top-headlines?'
        'q=medical&'
        'apiKey=81606bad15824906a328e56705cc8f52')
    response = requests.get(url)
    # print(response.json())
    results=response.json()['articles']
    # print(results)
    news=[]#title
    image=[]#url for image
    desc=[]#description
    content=[]
    urls=[]
    for l in range(len(results)):
        t=results[l]
        news.append(t['title'])
        image.append(t['urlToImage'])
        desc.append(t['description'])
        content.append(t['content'])
        urls.append(t['url'])
    mylist=zip(news,desc,content,image,urls)
    return render(request,'news.html',{'mylist':mylist})