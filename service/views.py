from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from .forms import UserRegisterationForm
from .models import Post
from django.urls import reverse_lazy

class HomePageView(TemplateView):
	template_name = "home.html"

class LoginView(View):
	
class  SignUpView(SuccessMessageminxin,CreateView):
	template_name = 'register'
	success_url = reverse_lazy('login')
	form_class = UserRegisterationForm
	success_message = 'You have successfully created an account with us.'
	

class CreatePostView(CreateView):
	model = Post
	template_name = 'newpost.html'

class EditPostView(UpdateView):
	model = Post
	template_name ='edit.html'

class DeletePostView(DeleteView):
	model = Post
	template_name = 'delete.html'
