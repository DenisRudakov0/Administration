from django import http
from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from .models import User, Client, Shop
import sqlite3


def index(request):
    try:
        print('OK')
    except:
        raise Http404('Ошибка внесения данных в БД')

# Create your views here.
