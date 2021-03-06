# Generated by Django 3.2.8 on 2021-11-09 14:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0025_auto_20211109_1503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='imageDate',
            field=models.DateField(default=datetime.datetime(2021, 11, 9, 16, 31, 34, 653243)),
        ),
        migrations.AlterField(
            model_name='user',
            name='birthDate',
            field=models.DateField(default=datetime.datetime(2021, 11, 9, 16, 31, 34, 652241)),
        ),
        migrations.AlterField(
            model_name='user',
            name='createdDate',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 9, 16, 31, 34, 652241)),
        ),
        migrations.AlterField(
            model_name='user',
            name='emailActvate',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
