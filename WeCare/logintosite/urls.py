from django.urls import path
from .views import login,authentication,logout

urlpatterns=[
    path('login/',login),
    path('authentication/',authentication),
    path('logout/',logout),
]