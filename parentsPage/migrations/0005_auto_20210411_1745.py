# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-04-11 14:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parentsPage', '0004_auto_20210411_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='subjectName',
            field=models.CharField(max_length=200),
        ),
    ]
