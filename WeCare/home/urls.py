from django.urls import path
from .views import index,doctorhome,adminhome,news,getprofile,updateprofile,gotosearch,search,hospitalsearch

urlpatterns=[
    path('',index),
    path('doctorhome/',doctorhome),
    path('adminhome/',adminhome),
    path('news/',news),
    path('getprofile/',getprofile),
    path('updateprofile/',updateprofile),
    path('gotosearch/',gotosearch),
    path('search/',search),
    path('hospitalsearch/',hospitalsearch),
]