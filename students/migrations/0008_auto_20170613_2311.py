# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-14 04:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0007_auto_20170613_2254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='Date of birth',
            field=models.DateField(blank=True),
        ),
    ]
