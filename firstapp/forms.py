from django import forms
from datetime import datetime, timedelta
from .models import *


class UserForm(forms.Form):
    TIME_CHOICES =  (
    ('22:00', "22:00"),
    ('21:00', "21:00"),
    ('20:00', "20:00"),
    ('19:00', "19:00"),
    ('18:00', "18:00"),
    ('17:00', "17:00"),
    ('16:00', "16:00"),
    ('15:00', "15:00"),
)

    name = forms.CharField(help_text="Введите свое имя", label='Имя')
    count_mans = forms.IntegerField(label='Количество человек', min_value=1, max_value=10)
    email = forms.CharField(required=False)
    type_room = forms.ChoiceField(choices=((1, "У окна"), (2, "Стандарт"), (3, "VIP")), label='Тип столика')
    breakfast = forms.BooleanField(required=False, label='Бонус от шефа?')
    phone = forms.CharField(label='Контактный телефон')
    # TODO: починить для поля ДАТЫ!
    date_s = forms.CharField(label="Дата брони", help_text="Введите дату в виде dd/мм/гггг")
    date_e = forms.ChoiceField(label="Время брони", choices=TIME_CHOICES)
