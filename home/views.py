from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import *
# Create your views here.		
	
def add_job_detail(request,slug):
	fields = Field.objects.all()
	if request.method=="POST":
		new_job_field = request.POST['field']
		f = Field.objects.get(name=new_job_field)
		f.save()
		job = Job.objects.get(name=slug)
		job.field=f
		job.save() 
		new_rev = Rev(content=request.POST['rev'], is_about=slug)
		new_rev.save()
		return HttpResponse(f"Thank You for {new_rev.content} about {slug}")
	context = {'field':fields}
	return render(request, 'home/add_job_detail.html', context)

def add_field_detail(request,slug):
	fields = Field.objects.all()
	if request.method=="POST":
		new_job_field = request.POST['field']
		f = Field.objects.get(name=new_job_field)
		f.save()
		job = Job(name=slug, field=f)
		job.save() 
		new_rev = Rev(content=request.POST['rev'], is_about=slug)
		new_rev.save()
		return HttpResponse(f"Thank You for {new_rev.content} about {slug}")
	context = {'field':fields}
	return render(request, 'home/add_job_detail.html', context)
		
def add_job(request):
	if request.method=="POST":
		job_name=request.POST['new_job']
		try:
			job = Job.objects.get(name=job_name)
			if job is not None:
				return HttpResponse(f'{job_name} is already here')
		except:
			new_job = Job(name=request.POST['new_job'])
			new_job.save()
			return render(request, 'home/add_job_successfully.html', {'new_job':new_job})	
	return render(request, 'home/add_job.html')	

def add_field(request):
	if request.method=="POST":
		field_name=request.POST['new_field']
		try:
			field = Field.objects.get(name=field_name)
			if field is not None:
				return HttpResponse(f'{field_name} is already here')
		except:
			new_field = Field(name=request.POST['new_field'])
			new_field.save()
			return render(request, 'home/add_field_successfully.html', {'new_field':new_field})	
	return render(request, 'home/add_field.html')	
					
def detail(request,slug):
	real_slug = slug[1:]
#the first part of our slug shows if we selected a job, a company or a category, so we parse 'em
	if request.method=='POST':
		new_rev = Rev(content = request.POST['new_rev'], is_about=real_slug)
		new_rev.save()
	j = Job(name=real_slug)
	field=j.field
	r = Rev.objects.filter(is_about=real_slug)
	try:
		return render(request, "home/detail.html", {'refs':r})
	except:
		return HttpResponse (request,"Nothings here")	
		
def home(request):
	job = Job.objects.all()
	company = Company.objects.all()
	field = Field.objects.all()
	context = {
		'job':job,
		'company':company,
		'field':field,
			}
	return render(request, 'home/home.html', context)
		

