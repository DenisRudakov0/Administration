# Generated by Django 3.2.4 on 2021-06-12 10:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0016_auto_20210612_1331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='shop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.client'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.client'),
        ),
    ]
