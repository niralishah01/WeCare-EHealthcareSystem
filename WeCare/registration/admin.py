from django.contrib import admin
from .models import SearchSymptomRecord,Doctor,SearchDiseaseResult,UserDetails
# Register your models here.
admin.site.register(SearchSymptomRecord)
admin.site.register(Doctor)
admin.site.register(SearchDiseaseResult)
admin.site.register(UserDetails)
