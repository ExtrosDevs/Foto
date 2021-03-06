# Generated by Django 3.2.8 on 2021-11-14 20:07

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0043_auto_20211114_2205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='user1',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.user'),
        ),
        migrations.AlterField(
            model_name='image',
            name='imageDate',
            field=models.DateField(default=datetime.datetime(2021, 11, 14, 22, 7, 19, 672231)),
        ),
        migrations.AlterField(
            model_name='user',
            name='createdDate',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 14, 22, 7, 19, 671231)),
        ),
    ]
