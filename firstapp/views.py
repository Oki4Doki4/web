from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.core import serializers
from .forms import UserForm
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
txt_dir = os.path.join(BASE_DIR, 'firstapp')
txt_dirr = os.path.join(txt_dir, 'dbb.txt')
#print(txt_dirr)
import datetime
import json
from django.core.serializers.json import DjangoJSONEncoder


def index(request):
    return render(request, "index.html")


def rest(request):
    return render(request, "rest.html")


def reserv(request):
    if request.method == 'GET':
        #userform = UserForm(request.POST)
        userform = UserForm()
    if request.method == "POST":
        userform = UserForm(request.POST)
        if userform.is_valid():

            name = request.POST.get("name")
            phone = request.POST.get("phone")
            email = request.POST.get("email")
            count_mans = request.POST.get("count_mans")
            breakfast = request.POST.get("breakfast")
            type_room = request.POST.get("type_room")
            date_s = request.POST.get('date_s')
            date_e = request.POST.get('date_e')

            if (type_room == "1"):
                type_room = "e"
            if (type_room == "2"):
                type_room = "s"
            if (type_room == "3"):
                type_room = "l"

            is_error = 0

            tmp_dict = {}
            tmp_dict['reserved_table'] = []
            tmp_dict['reserved_table'].append({
                "name": name,
                "date_s": date_s,
                "date_e": date_e,
                "email": email,
                "phone": phone,
                "type_room": type_room,
                "breakfast": breakfast,
                "count_mans": count_mans
            })

            save_data_s_e = userform.cleaned_data['date_s']
            save_data_e_s = userform.cleaned_data['date_e']
            para = (save_data_s_e, save_data_e_s)
            with open(txt_dirr, "r+") as out:
                for line in out:
                    if str(para) in line:
                        is_error = 1
                        break
                else:
                    out.write(str(para) + '\n')
            if is_error==1:
                return render(request, "err.html")

            return render(request, "comp.html",
                          {"name": name, "date_s": date_s, "date_e": date_e, "email": email,
                           "phone": phone, "type_room": type_room, "breakfast": breakfast, "count_mans": count_mans})
    else:
        userform = UserForm()
        return render(request, "res.html", {"form": userform})


'''
RECIPIENTS_EMAIL = ['']   # замените на свою почту
DEFAULT_FROM_EMAIL = ''
def contact_view(request):
    # если метод GET, вернем форму
    if request.method == 'GET':
        form = UserForm()
    elif request.method == 'POST':
        # если метод POST, проверим форму и отправим письмо
        form = UserForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['name']
            from_email = form.cleaned_data['email']
            message = form.cleaned_data['date_s'] + ' в '+ form.cleaned_data['date_e']
            try:
                send_mail(f'{subject} от {from_email}', f'столик забронирован на {message} ',
                          DEFAULT_FROM_EMAIL, RECIPIENTS_EMAIL)
            except BadHeaderError:
                return HttpResponse('Ошибка в теме письма.')
            return redirect('success')
    else:
        return HttpResponse('Неверный запрос.')
    return render(request, "email.html", {'form': form})

def success_view(request):
    return HttpResponse('Приняли! Спасибо за вашу заявку.')
'''''