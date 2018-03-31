from django.conf.urls import url
from . import views
from . import models


app_name= 'home'

urlpatterns = [
	#home/
	url(r'^$' , views.IndexView.as_view(), name='index'),
	
	#home/2
	url(r'^(?P<pk>[0-9]+)/$' , views.DetailView.as_view() , name ='detail' ) ,
	
	#home/addbook
	url(r'^add/$' , views.BookCreate.as_view(), name='create_book'),
	
	#home/2/update
	url(r'^(?P<pk>[0-9]+)/update$' , views.BookUpdate.as_view() , name ='update' ) ,
	
	#home/2/delete
	url(r'^(?P<pk>[0-9]+)/delete$' , views.BookDelete.as_view() , name ='delete' ) ,
	
	#home/logout
	url(r'^logout$' , views.IndexView.as_view(), name='logout_user'),
]