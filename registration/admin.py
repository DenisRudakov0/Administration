from django.contrib import admin
from .models import Client, Shop, User

admin.site.register(Client)
admin.site.register(User)
admin.site.register(Shop)
# Register your models here.
