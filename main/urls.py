from django.urls import path
from . import views
app_name='main'

urlpatterns = [
	path('',views.index,name='home'),
	path('contest/list',views.ContestList.as_view(),name='c-list'),
	path('contest/<int:pk>',views.ContestDetail.as_view(),name='c-detail'),
	path('contest/<int:pk>/submit',views.SubmitCreate.as_view(),name='s-create')



]
