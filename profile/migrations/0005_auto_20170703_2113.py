# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-03 18:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0004_auto_20170703_2038'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='profile',
            name='first_name',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='profile',
            name='last_name',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
