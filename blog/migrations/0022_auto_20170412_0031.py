# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-11 21:31
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0021_auto_20170401_2137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='key_expires',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 4, 12, 0, 31, 59, 718796)),
        ),
    ]