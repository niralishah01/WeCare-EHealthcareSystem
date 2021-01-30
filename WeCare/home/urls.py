from django.urls import path
from .views import index,doctorhome,adminhome,news

urlpatterns=[
    path('',index),
    path('doctorhome/',doctorhome),
    path('adminhome/',adminhome),
    path('news/',news),
]