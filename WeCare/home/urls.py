from django.urls import path
from .views import index,doctorhome,adminhome,hospitalsearch

urlpatterns=[
    path('',index),
    path('doctorhome/',doctorhome),
    path('hospitalsearch/',hospitalsearch),
    path('adminhome/',adminhome),
]