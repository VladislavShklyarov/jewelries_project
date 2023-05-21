from .models import Reply
from django.forms import ModelForm, TextInput, EmailInput


class ReplyForm(ModelForm):
    class Meta:
        model = Reply
        fields = ['name', 'email', 'text']

        widgets = {
            'name': TextInput (attrs={
                'class' : 'feedback_input',
                'placeholder' : 'ФИО',
            }),
            'email': TextInput (attrs={
                'class' : 'feedback_input',
                'placeholder' : 'Почта',
            }),'text': TextInput (attrs={
                'class' : 'feedback_input',
                'placeholder' : 'Что понравилось/ не понравилось',
            }),

        }