from django.urls import path
from . import views

urlpatterns = [
        path('',views.home, name='home'),
        #path("<single_slug>", views.single_slug, name="single_slug"),
        path('<category>', views.agencies_category, name="agencies_category")
]
