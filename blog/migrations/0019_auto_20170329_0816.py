# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-29 05:16
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_auto_20170329_0131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='key_expires',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 3, 29, 8, 16, 38, 688932)),
        ),
    ]
