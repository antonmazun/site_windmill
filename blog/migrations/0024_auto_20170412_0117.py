# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-11 22:17
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0023_auto_20170412_0115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='key_expires',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 4, 12, 1, 17, 43, 610737)),
        ),
    ]
