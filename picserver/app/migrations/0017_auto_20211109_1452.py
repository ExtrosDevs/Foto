# Generated by Django 3.2.8 on 2021-11-09 12:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_auto_20211109_1448'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='createdDate',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 9, 14, 52, 59, 164579)),
        ),
        migrations.AlterField(
            model_name='image',
            name='imageDate',
            field=models.DateField(default=datetime.datetime(2021, 11, 9, 14, 52, 59, 165591)),
        ),
        migrations.AlterField(
            model_name='user',
            name='birthDate',
            field=models.DateField(default=datetime.datetime(2021, 11, 9, 14, 52, 59, 163578)),
        ),
    ]
