# Generated by Django 3.2.8 on 2021-11-12 22:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0032_auto_20211113_0053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='imageDate',
            field=models.DateField(default=datetime.datetime(2021, 11, 13, 0, 54, 3, 967730)),
        ),
        migrations.AlterField(
            model_name='user',
            name='bio',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='birthDate',
            field=models.DateField(default=datetime.datetime(2021, 11, 13, 0, 54, 3, 966730)),
        ),
        migrations.AlterField(
            model_name='user',
            name='createdDate',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 13, 0, 54, 3, 966730)),
        ),
    ]
