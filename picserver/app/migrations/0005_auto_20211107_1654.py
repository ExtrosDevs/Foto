# Generated by Django 3.2.8 on 2021-11-07 14:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_user_birthdate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='c',
        ),
        migrations.AlterField(
            model_name='user',
            name='birthDate',
            field=models.DateField(default=datetime.datetime(2021, 11, 7, 16, 54, 17, 845233)),
        ),
    ]
