# Generated by Django 3.2.8 on 2021-11-17 19:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0049_auto_20211116_1257'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='private',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='image',
            name='imageDate',
            field=models.DateField(default=datetime.datetime(2021, 11, 17, 21, 54, 17, 585223)),
        ),
        migrations.AlterField(
            model_name='user',
            name='createdDate',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 17, 21, 54, 17, 584224)),
        ),
    ]
