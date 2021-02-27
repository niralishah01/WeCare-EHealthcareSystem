from django.urls import path
from .views import index,doctorhome,adminhome,hospitalsearch,news,getprofile,updateprofile,gotosearch,search

urlpatterns=[
    path('',index),
    path('doctorhome/',doctorhome),
    path('hospitalsearch/',hospitalsearch),
    path('adminhome/',adminhome),
    path('news/',news),
    path('getprofile/',getprofile),
    path('updateprofile/',updateprofile),
    path('gotosearch/',gotosearch),
    path('search/',search),
]