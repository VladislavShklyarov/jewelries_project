from django import forms
from django.forms import TextInput

from .models import Algorithm


class AlgorithmForm(forms.Form):
    class Meta:
        model = Algorithm

    D = forms.FloatField(label='Диаметр камня')
    A = forms.FloatField(label='Размер выреза')

