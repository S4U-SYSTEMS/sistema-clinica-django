from django.urls import path
from .views import ScheduleCreateView, ScheduleHomeView

app_name = 'schedule'

urlpatterns = [
    path('', ScheduleHomeView.as_view(), name='schedule_list'),
    path('agendamento/novo/', ScheduleCreateView.as_view(), name='schedule_create'),
]
