from django import forms
from main.models import *
from django.contrib.auth import get_user_model


class SubmissionForm(forms.ModelForm):
	
	class Meta:
		model=Submission
		fields='__all__'
