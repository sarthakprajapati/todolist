from django.db import models

# Create your models here.
class todolist(models.Model):
	title 		= models.CharField(max_length=20)
	description = models.CharField(max_length=200)
	date 		= models.DateField(auto_now=False, auto_now_add=False)
	active      = models.BooleanField(default=True)

	def __str__(self):
		return self.title
	def __unicode__(str):
		return self.title