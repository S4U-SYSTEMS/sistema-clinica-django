from bootstrap_modal_forms.forms import BSModalModelForm
from tempus_dominus.widgets import DateTimePicker

from .models import Schedule
from django import forms


class ScheduleForm(BSModalModelForm):
    def __init__(self, *args, **kwargs):
        super(ScheduleForm, self).__init__(*args, **kwargs)
        self.fields['Schedule_day'] = forms.DateTimeField(
            widget=DateTimePicker(
                options={
                    'useCurrent': True,
                    'collapse': False,
                },
                attrs={
                    'append': 'fa fa-calendar',
                    'icon_toggle': True,
                }
            ),
        )

    class Meta:
        model = Schedule
        fields = '__all__'

