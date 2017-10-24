# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-24 00:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('calculate', '0013_auto_20171023_1925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='section_course',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='calculate.Course'),
        ),
        migrations.AlterField(
            model_name='section',
            name='section_section',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='calculate.Section'),
        ),
    ]
