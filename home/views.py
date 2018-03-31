from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView 
from django.urls import reverse_lazy
from .models import book

class IndexView(generic.ListView):
	template_name='home/index.html'
	
	def get_queryset(self):
		return book.objects.all()


class DetailView(generic.DetailView):
	model=book
	template_name='home/detail.html'

class BookCreate(CreateView):
	model=book
	template_name='home/create_book.html'
	fields=['book_author','book_title','genre','book_logo']


class BookUpdate(UpdateView):
	model=book
	fields=['book_author','book_title','genre','book_logo']

class BookDelete(DeleteView):
	model=book
	success_url=reverse_lazy('home:index')

class UserFormView(DeleteView):
	form_class= UserFormView
	template_name='home/registration_form.html'

	def get(self, request):
		form=self.form_class(None)
		return render(request, self.template_name, {'form':form})

	def post(self, request):
		form=self.form_class(request.POST)

		if form.is_valid():
			user=form.save(commit= False)

			username=form.cleaned_data['username']
			password=form.cleaned_data['password']
			user.set_password(password)
			user.save()
