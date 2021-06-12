from django import http
from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect, HttpResponse
from .models import User, Client, Shop
import sqlite3


def index(request):
    return HttpResponse("Hello, World")

# Create your views here.
