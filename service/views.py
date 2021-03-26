from django.shortcuts import render
from .models import Agency
# Create your views here.

def homepage(request):
	agency = Agency.objects.all()
	context = {
		'agency': agency
	}
	return render(request, 'home.html', context)




