# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-04-11 13:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parentsPage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='submissions',
            field=models.FileField(upload_to='submissionsTasksKids/'),
        ),
    ]
