# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-19 22:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]