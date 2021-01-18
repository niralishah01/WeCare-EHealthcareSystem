from django.urls import path,include
from .views import getcoronaupdates
urlpatterns=[
    path('getcoronaupdates/',getcoronaupdates)
]