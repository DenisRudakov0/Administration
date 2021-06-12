from os import name
from django import http
from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect, HttpResponse
from .models import User, Client, Shop
import sqlite3
import datetime


def create(request):
    data = {
        'login': 'petr@mail.ru',
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

    Client.objects.all().delete()
    Shop.objects.all().delete()
    User.objects.all().delete()

    len_table = len(Client.objects.all()) + 1
    table_client = Client.objects.all()
    table_user = User.objects.all()
    table_shop = Shop.objects.all()

 
    if data['role'] == 'user':
        table_user.create(name = data['name'], email = data['email'], phone = data['phone'])
        table_shop.create()
    elif data['role'] == 'shop':
        date_registration = data['registration_date'].split('.')
        table_shop.create(name = data['name'], registration_number = data['registration_number'],
                          registration_date = datetime.date(*[int(i) for i in date_registration[::-1]]), physical_adress = data['physical_adress'],
                          lint = data['lint'], organization_person = data['organization_person'],
                          email = data['email'], phone = data['phone'])
        table_user.create()
    else:
        print('Упс! Вылезла какае-то ошибочка :)')
    table_client.create(login = data['login'], password = data['password'], 
                        id_shop = Shop.objects.id(), id_user = len_table)

    return HttpResponse(1)

# Create your views here.
