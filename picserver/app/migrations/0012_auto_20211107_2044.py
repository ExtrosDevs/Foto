# Generated by Django 3.2.8 on 2021-11-07 18:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20211107_2040'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='json',
            field=models.JSONField(default={'data': []}),
        ),
        migrations.AlterField(
            model_name='image',
            name='imageDate',
            field=models.DateField(default=datetime.datetime(2021, 11, 7, 20, 44, 24, 737654)),
        ),
        migrations.AlterField(
            model_name='user',
            name='birthDate',
            field=models.DateField(default=datetime.datetime(2021, 11, 7, 20, 44, 24, 737654)),
        ),
    ]
