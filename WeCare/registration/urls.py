from django.urls import path,include
from .views import getregsdetails,addregsdetails

urlpatterns=[
    path('getregsdetails/',getregsdetails),
    path('addregsdetails/',addregsdetails),
    # path('confirmation_mail/',confirmation_mail),
]