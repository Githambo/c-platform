from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin



from main.models import *
from main.forms import *

# Create your view;s here.
def index(request):
	template_name='base.html'
	return render(request,template_name)

class ContestList(ListView):
	model=Contest
	

class ContestDetail(DetailView):
	model=Contest

	def get_context_data(self,**kwargs):
		context=super(ContestDetail,self).get_context_data(**kwargs)
		context['submission']=Submission.objects.filter(contest=self.object).count()
		return context

class SubmitCreate(LoginRequiredMixin,CreateView,):
	form_class=SubmissionForm
	template_name='main/subcreate.html'

	def get_initial(self):
		initial=super().get_initial()
		initial['contest']=self.kwargs['pk']
		initial['user']=self.request.user
		return initial


	def form_valid(self,request):
		if self.request.method=='POST':
			form=SubmissionForm(self.request.POST,self.request.FILES)
			if form.is_valid():
				form.save()	
				return redirect('main:c-list')			
			return render(request,self.template_name,{'form':form})
		else:
			form=SubmissionForm()
			return render(request,self.template_name)