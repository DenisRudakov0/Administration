# Generated by Django 3.2.4 on 2021-06-12 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0007_auto_20210612_1124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Имя  продавца'),
        ),
    ]