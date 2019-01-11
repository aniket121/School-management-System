# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-26 19:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20170827_0118'),
    ]

    operations = [
        migrations.AddField(
            model_name='facultys',
            name='section',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='home.Sections'),
        ),
        migrations.AddField(
            model_name='students',
            name='section',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='home.Sections'),
        ),
    ]
