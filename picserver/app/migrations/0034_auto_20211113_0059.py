# Generated by Django 3.2.8 on 2021-11-12 22:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0033_auto_20211113_0054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='imageDate',
            field=models.DateField(default=datetime.datetime(2021, 11, 13, 0, 59, 50, 998905)),
        ),
        migrations.AlterField(
            model_name='user',
            name='birthDate',
            field=models.DateField(default=datetime.datetime(2021, 11, 13, 0, 59, 50, 997906)),
        ),
        migrations.AlterField(
            model_name='user',
            name='createdDate',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 13, 0, 59, 50, 997906)),
        ),
    ]
