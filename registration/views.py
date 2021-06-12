from os import name
from django import http
from django.db.models.fields import AutoField, Field
from django.db.models.fields.related import OneToOneField
from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect, HttpResponse
from .models import User, Client, Shop
import sqlite3
import datetime

def create(request):
    """   
    data = {
        'login': 'petr@mail.ru',
        'password': '123456',
        'role': 'user',
        'name': 'Ivan',
        'email': 'petr@mail.ru',
        'phone': '+243214566675'
    }
    """  
    data = {
        'login': 'ivanov@gmail.com',
        'password': '123456',
        'role': 'shop',
        'name': 'Ivan',
        'registration_number': '21312412412412',
        'registration_date': '12.02.2020',
        'physical_adress': 'ул. Пушкинская, д - 8',
        'lint': 'asasdadad',
        'organization_person': 'Пупкин Василий Иванович',
        'email': 'petr@mail.ru',
        'phone': '+243214566675'
    }
    
    len_table = len(Client.objects.all()) + 1
    table_client = Client.objects.all()
    table_user = User.objects.all()
    table_shop = Shop.objects.all()

    if data['role'] == 'user':
        id_user = create_user(request, data, table_user)
        Client.objects.create(login = data['login'], password = data['password'], user = User.objects.get(pk=id_user))
    elif data['role'] == 'shop':
        id_shop = create_shop(request, data, table_shop)
        Client.objects.create(login = data['login'], password = data['password'], shop = Shop.objects.get(pk=id_shop))
    else:
        print('Упс! Вылезла какае-то ошибочка :)')

    return HttpResponse(1)

def create_shop(request, data, table_shop):
    date_registration = data['registration_date'].split('.')
    w = Shop.objects.create(name = data['name'], registration_number = data['registration_number'],
                          registration_date = datetime.date(*[int(i) for i in date_registration[::-1]]),
                          physical_adress = data['physical_adress'],
                          lint = data['lint'], organization_person = data['organization_person'],
                          email = data['email'], phone = data['phone'])
    return w.id
    

def create_user(request, data, table_user):
    w = table_user.create(name = data['name'], email = data['email'], phone = data['phone'])
    return w.id
# Create your views here.
