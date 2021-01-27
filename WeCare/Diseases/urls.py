from django.urls import path
from .views import getdiseaseinfo,adddiseaseinfo,getsearchresults,viewdiseases,getupdateinfo,updatediseaseinfo
from django.views.generic import TemplateView

urlpatterns=[
    path('getdiseaseinfo/',getdiseaseinfo),
    path('adddiseaseinfo/',adddiseaseinfo),
    path('',TemplateView.as_view(template_name='searchresults.html'),name="searchpage"),
    path('getsearchresults/',getsearchresults),
    path('viewdiseases/',viewdiseases),
    path('getupdateinfo/',getupdateinfo),
    path('updatediseaseinfo/',updatediseaseinfo),
    #path('searchdiseases/',searchdiseases),
]