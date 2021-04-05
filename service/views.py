from django.views.generic import TemplateView
from django.shortcuts import render
from .models import Agency


def homepage(request):
	agency = Agency.objects.all()
	context = {
		'agency': agency
	}
	return render(request, 'home.html', context)


class HomePageView(TemplateView):
	template_name = "home.html"

