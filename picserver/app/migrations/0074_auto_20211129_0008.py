# Generated by Django 3.2.8 on 2021-11-28 22:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0073_auto_20211128_0107'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='firstName',
            field=models.CharField(default='unknown', max_length=30),
        ),
        migrations.AddField(
            model_name='user',
            name='lastName',
            field=models.CharField(default='unknown', max_length=30),
        ),
        migrations.AlterField(
            model_name='image',
            name='imageDate',
            field=models.DateField(default=datetime.datetime(2021, 11, 29, 0, 8, 15, 734170)),
        ),
        migrations.AlterField(
            model_name='image',
            name='tags',
            field=models.ManyToManyField(null=True, to='app.Tag'),
        ),
        migrations.AlterField(
            model_name='user',
            name='chats',
            field=models.ManyToManyField(null=True, to='app.Chat'),
        ),
        migrations.AlterField(
            model_name='user',
            name='createdDate',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 29, 0, 8, 15, 730172)),
        ),
        migrations.AlterField(
            model_name='user',
            name='following',
            field=models.ManyToManyField(null=True, related_name='_app_user_following_+', to='app.User'),
        ),
        migrations.AlterField(
            model_name='user',
            name='tagsLike',
            field=models.ManyToManyField(null=True, to='app.Tag'),
        ),
        migrations.AlterField(
            model_name='user',
            name='userstatus',
            field=models.BooleanField(default=False),
        ),
    ]
