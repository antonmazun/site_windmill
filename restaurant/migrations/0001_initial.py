# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-27 19:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=150)),
                ('weight', models.IntegerField()),
                ('price', models.IntegerField()),
                ('type', models.CharField(choices=[('фірмові страви', 'фірмові страви'), ('салат', 'салат'), ('холодні закуски', 'холодні закуски'), ('гарячі закуски', 'гарячі закуски'), ('перші страви', 'перші страви'), ('другі страви', 'другі страви'), ('гарніри', 'гарніри'), ('деруни', 'деруни'), ('десерти', 'десерти'), ('алкоголь', 'алкоголь'), ('чай', 'чай'), ('кава', 'кава')], max_length=30)),
            ],
        ),
    ]
