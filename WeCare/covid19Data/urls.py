from django.urls import path,include
from .views import getcoronaupdates,getname,coronaDetails,selectoption,getoption,allcountrydata
urlpatterns=[
    path('getcoronaupdates/',getcoronaupdates),
    path('getname/',getname),
    path('coronaDetails/',coronaDetails),
    path('selectoption/',selectoption),
    path('getoption/',getoption),
    path('allcountrydata/',allcountrydata),
]