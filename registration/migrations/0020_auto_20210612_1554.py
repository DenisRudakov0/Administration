# Generated by Django 3.2.4 on 2021-06-12 12:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0019_auto_20210612_1422'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='shop',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='registration.client'),
        ),
        migrations.AddField(
            model_name='user',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='registration.client'),
        ),
    ]