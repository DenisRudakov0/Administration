# Generated by Django 3.2.4 on 2021-06-12 06:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='id_shop',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='client',
            name='id_user',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='shop',
            name='id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='registration.client'),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='registration.client'),
        ),
    ]
