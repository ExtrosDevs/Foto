# Generated by Django 3.2.8 on 2021-12-10 23:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0078_auto_20211206_1418'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='views',
            field=models.ImageField(default=0, upload_to=''),
        ),
        migrations.AlterField(
            model_name='image',
            name='imageDate',
            field=models.DateField(default=datetime.datetime(2021, 12, 11, 1, 14, 56, 181921)),
        ),
        migrations.AlterField(
            model_name='user',
            name='createdDate',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 11, 1, 14, 56, 181921)),
        ),
    ]
