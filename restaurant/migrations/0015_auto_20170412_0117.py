# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-11 22:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0014_auto_20170412_0115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=models.ImageField(null=True, upload_to='image/'),
        ),
    ]