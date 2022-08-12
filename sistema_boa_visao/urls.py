from django.contrib import admin
from django.urls import path, include
from apps.home import urls as home_urls
from django.conf import settings
from django.conf.urls.static import static
from apps.patients import urls as patients_url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(home_urls)),
    path('pacientes/', include(patients_url)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
