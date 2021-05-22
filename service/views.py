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
		return HttpResponse(f"{single_slug} is a category") 

	agencies = [a.agancy_slug for a in Agency.objects.all()]
	if single_slug in agencies:
		return HttpResponse(f"{single_slug} is an Agency")

	return HttpResponse(f" '{single_slug}' does not correspond to anything we know of!")


