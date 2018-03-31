from django.db import models
from django.urls import reverse

# Create your models here.
class book(models.Model):
	book_title= models.CharField(max_length=250)
	book_author= models.CharField(max_length=250)
	price=models.IntegerField(default=0)
	genre=models.CharField(max_length=250)
	book_logo=models.FileField()
	is_favourite=models.BooleanField(default=False)
	
	def get_absolute_url(self):
		return reverse('home:detail', kwargs={'pk':self.pk})

##	def __str__ (self):
##		return str(self.book_title+'-'+self.book_author+'-'+self.price+'-'+self.genre);*/