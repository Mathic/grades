# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-24 22:58
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assignment_name', models.CharField(max_length=50)),
                ('is_section', models.BooleanField(default=False)),
                ('mark', models.IntegerField(default=0)),
                ('total', models.IntegerField(default=100)),
                ('percentage', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)])),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=50)),
                ('course_code', models.CharField(max_length=8, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='assignment',
            name='assignment_course',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='calculations.Course'),
        ),
        migrations.AddField(
            model_name='assignment',
            name='assignment_self',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='calculations.Assignment'),
        ),
    ]
