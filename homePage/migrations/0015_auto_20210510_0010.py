# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-05-09 21:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homePage', '0014_auto_20210509_2357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='submissions',
            field=models.FileField(upload_to='submissionsTasks'),
        ),
    ]