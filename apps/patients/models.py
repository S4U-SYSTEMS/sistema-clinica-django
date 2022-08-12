from apps.base.models import BaseModel
from django.db import models
from django.db.models import signals
from apps.base.signals import create_slug


class HealthInsurance(BaseModel):
    name = models.CharField('Nome', max_length=50)
    slug_from = 'name'

    def __str__(self):
        return self.name


class Patients(BaseModel):
    GENRE = (
        ('-', '-------'),
        ('M', 'Maculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
    )
    ETHNICITY = (
        ('-', '-------'),
        ('I', 'Indígena'),
        ('N', 'Negro'),
        ('B', 'Branco'),
        ('P', 'Pardo'),
        ('O', 'Outros'),
    )
    full_name = models.CharField('Nome Completo', max_length=100)
    social_name = models.CharField('Nome Social', max_length=100)
    birth_date = models.DateField('Nascimento')
    genre = models.CharField('Gênero', max_length=1, choices=GENRE, default='-')
    ethnicity = models.CharField('Etnia', max_length=1, choices=ETHNICITY, default='-')
    cpf = models.CharField('CPF', max_length=20)
    rg = models.CharField('RG', max_length=20)
    health_insurance = models.ForeignKey(HealthInsurance, verbose_name='Convênio', on_delete=models.CASCADE)
    slug_from = 'full_name'

    def __str__(self):
        return self.full_name


signals.post_save.connect(create_slug, sender=Patients)
signals.post_save.connect(create_slug, sender=HealthInsurance)
