from django.urls import path
from .views import index,doctorhome,adminhome,news,getprofile,updateprofile,gotosearch,search,hospitalsearch,pharmacysearch,viewdoctorprofiles,pharmacysearchnearest,hospitalsearchnearest

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
    path('pharmacysearch/',pharmacysearch),
    path('viewdoctorprofiles/',viewdoctorprofiles),
    path('pharmacysearchnearest/',pharmacysearchnearest),
    path('hospitalsearchnearest/',hospitalsearchnearest),
]