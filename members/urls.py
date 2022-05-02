from django.urls import path, re_path

from . import views


app_name = 'members'

urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^export/csv/$', views.export_data_csv, name='export_data_csv'),
    re_path(r'^export/xls/$', views.export_data_xls, name='export_data_xls'),


    
]