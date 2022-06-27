from django.db import models
from django.urls import reverse
# Create your models here.
# names should be stripped forms of string, cause are used as slug too. :/

class Field(models.Model):
	name = models.CharField(max_length=50)
	def __str__(self):
		return self.name
		
class Job(models.Model):
	name = models.CharField(max_length=50)	
	field = models.ForeignKey(Field, on_delete=models.CASCADE, null=True)
	def field_name(self):
		f = Field(id=self.field)
		return f.name	
	def __str__(self):
		return self.name
		
class Company(models.Model):
	name = models.CharField(max_length=50)
	def __str__(self):
		return self.name
						
class Rev(models.Model):
	content = models.TextField()
	is_about = models.CharField(max_length=200, null=True, blank=True)
	is_about_company = models.ForeignKey(Company, on_delete=models.CASCADE, null='0')	
	def __str__(self):
		return self.content
'''
class JobRev(models.Model):
	content = models.TextField()
	is_about = models.ForeignKey(Job, on_delete=models.CASCADE, blank=True, null='0' )
	def __str__(self):
		return self.content
		
class FieldRev(models.Model):
	content = models.TextField()
	is_about = models.ForeignKey(Field, on_delete=models.CASCADE, blank=True, null='0' )
	def __str__(self):
		return self.content
'''
