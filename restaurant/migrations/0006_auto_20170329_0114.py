# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-28 22:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0005_news'),
    ]

    operations = [
        migrations.CreateModel(
            name='News1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=1000)),
                ('img', models.ImageField(null=True, upload_to='image/')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='News',
        ),
    ]
