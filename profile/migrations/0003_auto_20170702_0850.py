# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-02 05:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0002_requestinfo'),
    ]

    operations = [
        migrations.DeleteModel(
            name='RequestInfo',
        ),
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_name',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]