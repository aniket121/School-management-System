# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-24 11:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_students_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='slug',
            field=models.SlugField(default='1', max_length=251),
        ),
    ]