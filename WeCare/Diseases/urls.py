from django.urls import path
from .views import getdiseaseinfo,adddiseaseinfo,getsearchresults,viewdiseases,getupdateinfo,updatediseaseinfo,homesearch,deletedisease,getsearchresults2
from .views import getskindiseaseinfo,addskindiseaseinfo,viewskindiseases,searchskindiseasefromimage,getdiseasetreatmentinfo,adddiseasetreatment,gettreatmentdetails,updatediseasetreatment
from django.views.generic import TemplateView

urlpatterns=[
    path('getdiseaseinfo/',getdiseaseinfo),
    path('getskindiseaseinfo/',getskindiseaseinfo),
    path('adddiseaseinfo/',adddiseaseinfo),
    path('',TemplateView.as_view(template_name='searchresults.html'),name="searchpage"),
    path('',TemplateView.as_view(template_name='searchresults2.html'),name="treatmentsearchpage"),
    path('getsearchresults/',getsearchresults),
    path('getsearchresults2/',getsearchresults2),
    path('viewdiseases/',viewdiseases),
    path('getupdateinfo/',getupdateinfo),
    path('updatediseaseinfo/',updatediseaseinfo),
    path('deletedisease/',deletedisease),
    #path('searchdiseases/',searchdiseases),
    path('homesearch/',homesearch),
    path('addskindiseaseinfo/',addskindiseaseinfo),
    path('viewskindiseases/',viewskindiseases),
    path('searchskindiseasefromimage/',searchskindiseasefromimage),
    path('getdiseasetreatmentinfo/',getdiseasetreatmentinfo),
    path('adddiseasetreatment/',adddiseasetreatment),
    path('gettreatmentdetails/',gettreatmentdetails),
    path('updatediseasetreatment/',updatediseasetreatment),
    path('',TemplateView.as_view(template_name='searchresults2.html'),name="treatmentsearchpage"),
]