# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-20 02:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('calculate', '0008_auto_20171019_2210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='section_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='section', to='calculate.Section'),
        ),
    ]