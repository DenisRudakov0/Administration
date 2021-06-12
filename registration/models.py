from django.db import models

class Client(models.Model):
    login = models.CharField("Имя продавца", max_length=50)
    password = models.CharField("Имя продавца", max_length=50)
    id_shop = models.IntegerField()
    id_user = models.IntegerField() 
    
class User(models.Model):
    id = models.OneToOneField(Client, on_delete = models.CASCADE, primary_key = True)
    name = models.CharField("Имя пользователя", max_length=50)
    email = models.CharField("Почта", max_length=50)
    phone = models.CharField("Телефон", max_length=20)

class Shop(models.Model):
    id = models.OneToOneField(Client, on_delete = models.CASCADE, primary_key = True)
    name = models.CharField("Имя продавца", max_length=50)
    registration_number = models.CharField("Регистрационный номер", max_length=50)
    registration_date = models.DateField("Дата регистрации")
    physical_adress = models.CharField("Физический адресс", max_length=200)
    lint = models.CharField("?", max_length=50)
    organization_person = models.CharField("Имя организации", max_length=50)
    email = models.CharField("Почта продавца", max_length=50)
    phone = models.CharField("Телефон продавца", max_length=50)


