from django import forms
from .models import Request


class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ['name','message','email']
        labels = {'name': 'Ваше имя:', 'message': 'Изложите пожелания:','email': 'Уникальный емейл:'}