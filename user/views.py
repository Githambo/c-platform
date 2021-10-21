from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse

# Create your views here.
class RegisterView(CreateView):
	form_class=UserCreationForm
	template_name='register.html'
	success_url=reverse('main:home')