from django.contrib import admin
from .models import Agency,Category
#from tinymce import TinyMCE
from django.db import models
#from tinymce import TinyMCE
# Register your models here.

class categoryAdmin(admin.ModelAdmin):
    list_display=["category","cover_tag"]
    readonly_fields=["cover_tag"]



class agencyAdmin(admin.ModelAdmin):
    list_display = ["Title","image_tag","Added"]

    readonly_fields=["image_tag"]


   # formfield_overrides = {
   #         models.TextField: {'widget': TinyMCE()}
   #     }

admin.site.register(Category, categoryAdmin)
admin.site.register(Agency, agencyAdmin)    