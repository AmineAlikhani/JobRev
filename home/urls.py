from django.urls import path, include
from . import views

app_name = 'home'

urlpatterns = [
	path('', views.home, name='home'),	
	path('add_job', views.add_job, name='add_job'),
	path('add_field', views.add_field, name='add_field'),
	path('add_job_detail/<slug:slug>', views.add_job_detail, name='add_job_detail'),
#	path('add_field_detail/<slug:slug>', views.add_field_detail, name='add_field_detail'),
	path('detail/<slug:slug>', views.detail, name='detail'),
]
