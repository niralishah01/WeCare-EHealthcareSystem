from django.urls import path
from .views import index,doctorhome,adminhome

urlpatterns=[
    path('',index),
    path('doctorhome/',doctorhome),
    path('adminhome/',adminhome),
]