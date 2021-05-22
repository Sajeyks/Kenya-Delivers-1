from django.contrib import admin
from .models import Agency,agencyCategory
#from tinymce import TinyMCE
from django.db import models
#from tinymce import TinyMCE
# Register your models here.


class agencyAdmin(admin.ModelAdmin):
   list_display = ["image_tag","agency_Title","agency_Category","agency_Added"]
   ordering = ["agency_Added"] 
   readonly_fields=["image_tag"]
   
   # formfield_overrides = {
   #         models.TextField: {'widget': TinyMCE()}
   #     }

admin.site.register(agencyCategory)
admin.site.register(Agency, agencyAdmin)    