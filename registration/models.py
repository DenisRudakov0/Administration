from django.db import models

class Client(models.Model):
    login = models.CharField("Имя продавца", max_length=50, unique=True)
    password = models.CharField("Имя продавца", max_length=50)
    user = models.OneToOneField('User', on_delete = models.CASCADE, null=True)
    shop = models.OneToOneField('Shop', on_delete = models.CASCADE, null=True)

    def __str__(self):
        return self.login

class User(models.Model):
    name = models.CharField("Имя пользователя", max_length=50)
    email = models.CharField("Почта", max_length=50)
    phone = models.CharField("Телефон", max_length=20)

    def __str__(self):
        return self.name

class Shop(models.Model):
    name = models.CharField("Имя продавца", max_length=50)
    registration_number = models.CharField("Регистрационный номер", max_length=50)
    registration_date = models.DateField("Дата регистрации")
    physical_adress = models.CharField("Физический адресс", max_length=200)
    lint = models.CharField("?", max_length=50)
    organization_person = models.CharField("Имя организации", max_length=50)
    email = models.CharField("Почта продавца", max_length=50)
    phone = models.CharField("Телефон продавца", max_length=50)

    def __str__(self):
        return self.name   


