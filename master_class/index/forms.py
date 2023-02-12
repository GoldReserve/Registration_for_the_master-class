from django import forms
from .models import *

GEEKS_CHOICES = (
    ("1", "№1 Делаем с Риткой жаркое"),
    ("2", "№2 Светодиодная подсветка"),
    ("3", "№3 Выращиваем всякое вертикально"),
    ("4", "№4 Деревянная шкатулка"),
    ("5", "№5 Литье эпоксидной смолой"),
)


class MasterClassRegistration(forms.Form):
    name = forms.CharField(max_length=100, label='ФИО')
    number = forms.IntegerField(label='Тел')
    master_class = forms.ChoiceField(choices=GEEKS_CHOICES, label='Вид')
    date = forms.CharField(label='Дата')
    email = forms.EmailField(label='Email')
