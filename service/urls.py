from django.urls import path
from . import views

urlpatterns = [
        path('',views.homepage, name='home'),
        path('<category>', views.agencies_category, name="agencies_category"),
        path('search/', views.searchResults,name="searchResults")
        
]
