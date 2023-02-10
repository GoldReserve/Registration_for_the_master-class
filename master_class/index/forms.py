from django import forms
from .models import *

class MasterClassRegistration(forms.Form):
    name = forms.CharField(max_length=100, label='ФИО')
    number = forms.IntegerField(label='Тел.')
    date = forms.DateTimeField(label='Дата')
    email = forms.EmailField(label='Email')