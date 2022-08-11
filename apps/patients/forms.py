from .models import Patients
from bootstrap_modal_forms.forms import BSModalModelForm
from django import forms
from tempus_dominus.widgets import DatePicker


class PatientsForm(BSModalModelForm):
    def __init__(self, *args, **kwargs):
        super(PatientsForm, self).__init__(*args, **kwargs)
        self.fields['birth_date'] = forms.DateField(
            widget=DatePicker(
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
        model = Patients
        fields = '__all__'
