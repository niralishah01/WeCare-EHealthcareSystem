from django.urls import path
from .views import login,authentication

urlpatterns=[
    path('login/',login),
    path('authentication/',authentication),
]