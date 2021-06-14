from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Agency,agencyCategory
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def homepage(request):
	
		return render(
			request=request,
			template_name='categories.html',
			context={"categories": agencyCategory.objects.all(),
			         "popular": Agency.objects.filter(is_porpular = "True" ),
			
			}
		)


def agencies_category(request, category):
	agents = Agency.objects.filter(agency_Category__agency_Category__contains=category)
	page = request.GET.get('page',1)

	paginator = Paginator(agents, 15)
	try:
		agencies = paginator.page(page)
	except PageNotAnInteger:
		agencies = paginator.page(1)
	except EmptyPage:
		agencies = paginator.page(paginator.num_pages)		


	context = {
		'category': category,
		'agencies': agencies,
	}
	

	return render(request, "agencies.html", context)


def searchResults(request):
	search_agency = request.GET.get('search')

	if search_agency:
		agency = Agency.objects.filter(Q(agency_Title__icontains=search_agency )) # | Q(agency_Description__icontains=search_agency))
		
	else:
		agency = Agency.objects.all()	


	if not agency:
		return HttpResponse("OOPS!! We couldnt find any match for your search...")
	
	else:
		return render(request, "search.html", {'agency':agency})	

	

	