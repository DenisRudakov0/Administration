from os import name
from django import http
from django.db.models.fields import AutoField, Field
from django.db.models.fields.related import OneToOneField
from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect, HttpResponse
from .models import User, Client, Shop
import datetime
import ast

def create(request):  

    data = request.GET['data']
    data = ast.literal_eval(data)

    try:
        if Client.objects.filter(login = data['login']).exists() == True:
            return HttpResponse('Пользователь с данным логином уже зарегистрирован')
        if data['role'] == 'user':
            id_user = create_user(request, data)
            Client.objects.create(login = data['login'], password = data['password'], user = User.objects.get(pk=id_user))
        elif data['role'] == 'shop':
            id_shop = create_shop(request, data)
            Client.objects.create(login = data['login'], password = data['password'], shop = Shop.objects.get(pk=id_shop))
        else:
            return HttpResponse('Упс! Возникла ошибочка при определении роли')
        return HttpResponse('Данные успешно добавлены :)')
    except:      
        return HttpResponse('Упс! Возникла неизвестная ошибочка, попробуйте снова чуть-чуть по-позже')

def create_shop(request, data):
    date_registration = data['registration_date'].split('.')
    create_shop = Shop.objects.create(name = data['name'], registration_number = data['registration_number'],
                          registration_date = datetime.date(*[int(i) for i in date_registration[::-1]]),
                          physical_adress = data['physical_adress'],
                          lint = data['lint'], organization_person = data['organization_person'],
                          email = data['email'], phone = data['phone'])
    return create_shop.id

def create_user(request, data):
    create_user = User.objects.create(name = data['name'], email = data['email'], phone = data['phone'])
    return create_user.id


