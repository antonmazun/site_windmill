# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-28 20:43
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20170327_2054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='key_expires',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 3, 28, 23, 43, 37, 181032)),
        ),
    ]
