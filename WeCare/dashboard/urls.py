from django.urls import path
from .views import gotodashboard,dashboard1,dashboard2,pivot_data,pivot_data2,selectoption,export_csv,export_pdf,export_csv2

urlpatterns=[
    path('gotodashboard/',gotodashboard),
    path('selectoption/',selectoption),
    path('dashboard1/',dashboard1),
    path('dashboard2/',dashboard2),
    path('pivot_data',pivot_data),
    # path('data',pivot_data,name='pivot_data'),
    path('data2',pivot_data2,name='pivot_data2'),
    path('export_csv/',export_csv),
    path('export_csv2/',export_csv2),
    path('export_pdf/',export_pdf)
]
    