from django.contrib import admin
from .models import Agency
from tinymce.widgets import TinyMCE
from django.db import models
#from tinymce import TinyMCE
# Register your models here.


class agencyAdmin(admin.ModelAdmin):
    list_display = ["Title","image_tag","Added"]

    readonly_fields=["image_tag"]


   # formfield_overrides = {
   #         models.TextField: {'widget': TinyMCE()}
   #     }

admin.site.register(Agency, agencyAdmin)    