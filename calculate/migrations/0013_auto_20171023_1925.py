# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-23 23:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculate', '0012_auto_20171023_0043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_code',
            field=models.CharField(max_length=8),
        ),
    ]
