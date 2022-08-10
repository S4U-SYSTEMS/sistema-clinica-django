from django.urls import reverse_lazy
from .forms import PatientsForm
from django.views.generic.list import ListView
from django.contrib.messages.views import SuccessMessageMixin
from bootstrap_modal_forms.generic import BSModalCreateView

from .models import Patients


class PatientCreateView(BSModalCreateView):
    template_name = 'patients/create_patients.html'
    form_class = PatientsForm
    success_message = 'Success: Paciente criado.'
    success_url = reverse_lazy('patients:patient_list')


class PatientListView(SuccessMessageMixin, ListView):
    model = Patients
    success_message = 'Success: Paciente criado.'
    context_object_name = 'patients'
    template_name = 'patients/list_patients.html'


