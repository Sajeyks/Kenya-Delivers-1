
from django.contrib import admin
from django.urls import path, include

from .import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', include('service.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('tinymce/',include('tinymce.urls')),
]

urlpatterns +=staticfiles_urlpatterns()
urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "K-Delivers"
admin.site.site_title = "K-Delivers Admin Portal"
admin.site.index_title = "Welcome to K-Delivers Portal"
