from django.urls import path

from . import views

app_name = 'viz'

urlpatterns = [
	#<type:columnName>/path/ | views.FuncName | name=fileName
    path('', views.index, name='index'),
    path('tracts/', views.tracts, name='tracts'),
    path('tracts/<int:tract_id>/', views.tracts_site, name='tracts_site'),
    path('sites/', views.sites, name='sites'),
    path('pie/', views.pie, name='pie'),
    path('bar/', views.bar, name='bar'),
]
#https://stackoverflow.com/questions/36804879/django-detailview-filtering-object-based-off-primary-key
