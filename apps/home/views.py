from django.views.generic.base import TemplateView
from apps.schedule.models import Schedule


class HomeView(TemplateView):
    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['schedules'] = Schedule.objects.todays_appointments()
        context['cont_appointments'] = Schedule.objects.cont_appointments()
        context['completed_appointments'] = Schedule.objects.completed_appointments()
        return context
