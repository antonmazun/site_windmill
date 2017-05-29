# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-01 18:37
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0020_auto_20170401_2133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='name',
            field=models.CharField(max_length=10000),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='key_expires',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 4, 1, 21, 37, 57, 190272)),
        ),
    ]