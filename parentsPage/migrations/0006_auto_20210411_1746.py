# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-04-11 14:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parentsPage', '0005_auto_20210411_1745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='subjectName',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homePage.subject'),
        ),
    ]
