# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-29 17:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0003_auto_20170629_1705'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedules',
            name='schedule_id',
            field=models.IntegerField(null=True),
        ),
    ]
