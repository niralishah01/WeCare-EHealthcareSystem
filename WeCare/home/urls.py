from django.urls import path
from .views import index,doctorhome,adminhome,news,getprofile,updateprofile

urlpatterns=[
    path('',index),
    path('doctorhome/',doctorhome),
    path('adminhome/',adminhome),
    path('news/',news),
    path('getprofile/',getprofile),
    path('updateprofile/',updateprofile),
]