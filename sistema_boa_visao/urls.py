from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from apps.home import urls as home_urls
from apps.patients import urls as patients_url
from apps.schedule import urls as schedule_url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(home_urls)),
    path('pacientes/', include(patients_url)),
    path('agendamentos/', include(schedule_url)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
