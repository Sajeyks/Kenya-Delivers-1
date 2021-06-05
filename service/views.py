from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Agency,agencyCategory


def homepage(request):
	
		return render(
			request=request,
			template_name='categories.html',
			context={"categories": agencyCategory.objects.all(),
			         "popular": Agency.objects.filter(is_porpular = "True" ),
			
			}
		)


def agencies_category(request, category):
	agencies = Agency.objects.filter(
		agency_Category__agency_Category__contains=category

	)

	context = {
		'category': category,
		'agencies': agencies,
		
	}
	
	
	return render(request, "agencies.html", context)
