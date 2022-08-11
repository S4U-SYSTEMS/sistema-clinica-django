from django.db import models
from safedelete.models import SafeDeleteModel
from django.utils import timezone

from safedelete.models import SOFT_DELETE
from django.db.models import signals
from apps.base.models import BaseModel
from apps.base.signals import create_slug
from apps.patients.models import Patients


class ScheduleManager(models.Manager):

    def not_concluded(self):
        return self.filter(concluded=False)

    def todays_appointments(self):
        now = timezone.now().day
        date = self.filter(Schedule_day__day=now).filter(concluded=False)

        return date

    def cont_appointments(self):
        now = timezone.now().day
        return self.filter(Schedule_day__day=now).filter(concluded=False).count()

    def completed_appointments(self):
        now = timezone.now().day
        return self.filter(Schedule_day__day=now).filter(concluded=True).count()


class Schedule(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE

    patient = models.ForeignKey(Patients, on_delete=models.CASCADE, verbose_name='Paciente',
                                related_name='schedule_patient')
    Schedule_day = models.DateTimeField('Data')
    concluded = models.BooleanField('Concluído', default=False)
    created_at = models.DateTimeField(
        'Cadastrado em', auto_now_add=True, null=True)
    updated_at = models.DateTimeField(
        'Modificado em', auto_now=True, null=True)

    objects = ScheduleManager()

    def __str__(self):
        return self.Schedule_day


signals.post_save.connect(create_slug, sender=Schedule)
