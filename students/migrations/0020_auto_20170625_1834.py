# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-25 18:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0019_auto_20170620_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_id',
            field=models.CharField(blank=True, max_length=128, null=True, unique=True),
        ),
    ]
