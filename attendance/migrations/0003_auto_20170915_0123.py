# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-14 19:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0002_auto_20170912_0303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daily_attendance',
            name='faculty',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='daily_attendance',
            name='section',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='daily_attendance',
            name='student',
            field=models.IntegerField(),
        ),
    ]
