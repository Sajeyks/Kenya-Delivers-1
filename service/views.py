from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Agency,agencyCategory


def home(request):
		return render(
			request=request,
			template_name='categories.html',
			context={"categories": agencyCategory.objects.all()}
		)

def homepage(request):
		agency = Agency.objects.all()
		context = {
			'agency': agency
		}
		return render(request, 'home.html', context)


def single_slug(request, single_slug):
		categories = [c.category_slug for c in agencyCategory.objects.all()]
		if single_slug in categories:
			#return HttpResponse(f"{single_slug} is a category")
			matching_agencies = Agency.objects.get(agency_Category=single_slug)
			return HttpResponse(f"{matching_agencies} is a category")

			#return render(
			#	request = request,
			#	template_name= 'agencies.html',
			#	context= {"agencies": matching_agencies}
			#)

		agencies = [a.agancy_slug for a in Agency.objects.all()]
		if single_slug in agencies:
			return HttpResponse(f"{single_slug} is an Agency")

		return HttpResponse(f" '{single_slug}' does not correspond to anything we know of!")


def agencies_category(request, category):
	agencies = Agency.objects.filter(
		agency_Category__agency_Category__contains=category

	)
	context = {
		'category': category,
		'agencies': agencies
	}
	
	return render(request, "agencies.html", context)
