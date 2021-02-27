from django.urls import path
from .views import getdiseaseinfo,adddiseaseinfo,viewskindiseases,getsearchresults,viewdiseases,getupdateinfo,updatediseaseinfo,homesearch,addskindiseaseinfo,getskindiseaseinfo
from django.views.generic import TemplateView

urlpatterns=[
    path('getdiseaseinfo/',getdiseaseinfo),
    path('getskindiseaseinfo/',getskindiseaseinfo),
    path('adddiseaseinfo/',adddiseaseinfo),
    path('',TemplateView.as_view(template_name='searchresults.html'),name="searchpage"),
    path('getsearchresults/',getsearchresults),
    path('viewdiseases/',viewdiseases),
    path('getupdateinfo/',getupdateinfo),
    path('updatediseaseinfo/',updatediseaseinfo),
    #path('searchdiseases/',searchdiseases),
    path('homesearch/',homesearch),
    path('addskindiseaseinfo/',addskindiseaseinfo),
    path('viewskindiseases/',viewskindiseases),
]