# Generated by Django 3.2.4 on 2021-06-12 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0008_alter_shop_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Имя продавца'),
        ),
    ]
