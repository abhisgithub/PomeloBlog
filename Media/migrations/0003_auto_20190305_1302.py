# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-05 13:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Media', '0002_auto_20190305_1025'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='media',
            name='city',
        ),
        migrations.RemoveField(
            model_name='media',
            name='location',
        ),
        migrations.RemoveField(
            model_name='media',
            name='medialink',
        ),
        migrations.RemoveField(
            model_name='media',
            name='views',
        ),
        migrations.AddField(
            model_name='media',
            name='latitude',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='media',
            name='longitude',
            field=models.TextField(null=True),
        ),
    ]
