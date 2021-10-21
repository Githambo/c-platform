from django.db import models
import datetime
from django.conf import settings

# Create your models here.

class Contest(models.Model):	
	STATUS=(
		('active','active'),
		('closed','closed'),	)

	title=models.CharField(max_length=200,unique=True)	
	image=models.ImageField(upload_to='contest_images',blank=True)	
	description=models.TextField(max_length=1000)
	date_of_posting=models.DateField(default=datetime.date.today)
	status=models.TextField(choices=STATUS,default='active')	

	def __str__(self):
		return '{}'.format(self.title)

	def subs(self):
		subs=Submission.objects.filter(contest=self.id).count()
		return subs

class Submission(models.Model):
	user=models.ForeignKey(
		to=settings.AUTH_USER_MODEL,
		on_delete=models.CASCADE
		)
	contest=models.ForeignKey(
		to=Contest,
		on_delete=models.CASCADE
		)
	description=models.TextField(max_length=1000)
	image=models.ImageField(upload_to='submission_images',blank=True)
	date=models.DateField(default=datetime.date.today)