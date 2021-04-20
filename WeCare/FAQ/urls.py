from django.urls import path
from .views import getquestioninfo,postquestion,viewquestion,postanswer,viewanswer,addanswer,deletequestion,allquestions,viewFAQ
from django.views.generic import TemplateView

urlpatterns=[
    path('getquestioninfo/',getquestioninfo),
    path('postquestion/',postquestion),
    path('viewquestion/',viewquestion),
    path('postanswer/',postanswer),
    path('viewanswer/',viewanswer),
    path('addanswer/',addanswer),
    path('deletequestion/',deletequestion),
    path('allquestions/',allquestions),
    path('viewFAQ/',viewFAQ),
]