from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail, BadHeaderError
from django.contrib import auth
from django.views.decorators import csrf
from django import forms
from restaurant.models import Comments

from .forms import ContactForm, User, UserCreationForm
from .models import UserProfile
from django.db import models
from datetime import datetime
from django.template import RequestContext
from django.core.mail import send_mail
import hashlib, datetime, random
from django.utils import timezone


def contactform(reguest):
    result = "Дякуюємо , що залишили своє повідомлення, адміністратор зв’яжеться з вами!"
    if reguest.method == 'POST':
        form = ContactForm(reguest.POST)
        # Если форма заполнена корректно, сохраняем все введённые пользователем значения
        if form.is_valid():
            subject = form.cleaned_data['subject']
            sender = form.cleaned_data['sender']
            message = form.cleaned_data['message']
            copy = form.cleaned_data['copy']
            phone = form.cleaned_data['phone']
            date = form.cleaned_data['date']
            people = form.cleaned_data['people']

            message = "Cообщение %s \n" % reguest.POST['message']
            message += "Отправитель %s \n " % reguest.POST['sender']
            message += "Номер замовника %s \n " % reguest.POST['phone']
            message += "Дата проведення банкету %s \n" % reguest.POST['date']
            message += "Кількість людей %s \n " % reguest.POST['people']

            recepients = ['kpi.study1@gmail.com']
            # Если пользователь захотел получить копию себе, добавляем его в список получателей
            if copy:
                recepients.append(sender)
            try:
                send_mail(subject, message, 'kpi.study1@gmail.com', recepients)
            except BadHeaderError:  # Защита от уязвимости
                return HttpResponse('Invalid header found')
            # Переходим на другую страницу, если сообщение отправлено
            return render(reguest, "home.html", {'result': result})

    else:
        form = ContactForm()
    # Выводим форму в шаблон
    return HttpResponse('не работает')


# def thanks(reguest):
#     thanks = 'thanks'
#     return render(reguest, 'thanks.html', {'thanks': thanks})


def news(request):
    if request.method == "GET":
        return render(request, "news.html", {})


def about_us(request):
    if request.method == "GET":
        return render(request, "about_us.html", {'comments': Comments.objects.all()})


def gallery(request):
    return render(request, "gallery.html", {})


def show(request):
    arg = {}
    return render(request, 'home.html', arg)

#
# def register_user(request):
#     args = {}
#    # args.update(csrf(request))
#     if request.method == 'POST':
#         form = RegistrationForm(request.POST)
#         args['form'] = form
#         if form.is_valid():
#             form.save()
#
#             username = form.cleaned_data['username']
#             email = form.cleaned_data['email']
#             salt = hashlib.sha1(str(random.random())).hexdigest()[:5]
#             activation_key = hashlib.sha1(salt + email).hexdigest()
#             key_expires = datetime.now() + datetime.timedelta(2)
#
#             user = User.objects.get(username = username)
#             new_profile = UserProfile(user=user, activation_key=activation_key,key_expires=key_expires)
#             new_profile.save()
#
#             # Send email with activation key
#             email_subject = 'Подтверждение регистрации'
#             email_body = "Привет %s, thanks for signing up. To activate your account, click this link within \
#             48hours http://127.0.0.1:8082/accounts/confirm/%s" % (username, activation_key)
#
#             send_mail(email_subject, email_body, 'myemail@example.com',[email], fail_silently=False)
#
#             return HttpResponseRedirect('accounts/register_success')
#         else:
#             args['form'] = RegistrationForm()
#             return render_to_response('user_profile/register.html'  ,args , context_instance = RequestContext(request))
#     return render(request , 'register.html' , {})

#
# def register_confirm(request, activation_key):
#     if request.user.is_authenticated():
#         HttpResponseRedirect('/')
#
#         user_profile = get_object_or_404(UserProfile, activation_key=activation_key)
#
#         if user_profile.key_expires < timezone.now():
#             return render_to_response('user_profile/confirm_expired.html')
#         user = user_profile.user
#         user.is_active = True
#         user.save()
#         return render_to_response('user_profile/confirm.html')
#
#
