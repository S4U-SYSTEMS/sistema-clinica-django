from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from bootstrap_modal_forms.generic import BSModalCreateView

from .models import Schedule
from .forms import ScheduleForm


class ScheduleCreateView(BSModalCreateView):
    template_name = 'schedule/create_schedule.html'
    form_class = ScheduleForm
    success_message = 'Success: Agendamento criado.'
    success_url = reverse_lazy('schedule:schedule_list')


class ScheduleHomeView(TemplateView):
    template_name = 'schedule/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['schedules'] = Schedule.objects.not_concluded()

        return context
