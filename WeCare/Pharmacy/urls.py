from django.urls import path
from django.views.generic import TemplateView
from .views import getpharmacyinfo,getpharmacy,viewpharmacy,addpharmacyinfo,getupdatedpharmacyinfo,updatepharmacyinfo,deletepharmacy

urlpatterns=[
    path('getpharmacyinfo/',getpharmacyinfo),
    path('getpharmacy/',getpharmacy),
    path('addpharmacyinfo/',addpharmacyinfo),
    path('viewpharmacy/',viewpharmacy),
    path('getupdatedpharmacyinfo/',getupdatedpharmacyinfo),
    path('updatepharmacyinfo/',updatepharmacyinfo),
    path('deletepharmacy/',deletepharmacy)

]