# Generated by Django 3.2.8 on 2021-11-27 23:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0072_auto_20211128_0105'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='mas',
        ),
        migrations.AlterField(
            model_name='image',
            name='imageDate',
            field=models.DateField(default=datetime.datetime(2021, 11, 28, 1, 7, 35, 808900)),
        ),
        migrations.RemoveField(
            model_name='image',
            name='tags',
        ),
        migrations.AddField(
            model_name='image',
            name='tags',
            field=models.ManyToManyField(to='app.Tag'),
        ),
        migrations.AlterField(
            model_name='user',
            name='createdDate',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 28, 1, 7, 35, 803903)),
        ),
    ]
