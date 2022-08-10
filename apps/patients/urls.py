from django.urls import path
from .views import PatientCreateView, PatientListView

app_name = 'patients'

urlpatterns = [
    path('', PatientListView.as_view(), name='patient_list'),
    path('paciente/novo/', PatientCreateView.as_view(), name='patient_create'),
]
