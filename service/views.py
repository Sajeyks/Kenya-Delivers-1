#from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
#def index(requests):
#	return render(requests, "service/templates/index.html",)
class HomePageView(TemplateView):
	template_name = "home.html"