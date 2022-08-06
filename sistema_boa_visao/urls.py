from django.contrib import admin
from django.urls import path, include
from apps.base import urls as base_url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(base_url)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
