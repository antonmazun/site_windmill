# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-27 16:29
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20170326_1454'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish',
            name='image',
            field=models.ImageField(default='image/images.jpg', null=True, upload_to='image/'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='key_expires',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 3, 27, 19, 29, 9, 621875)),
        ),
    ]
