# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-05-14 06:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homePage', '0013_delete_submission'),
    ]

    operations = [
        migrations.CreateModel(
            name='reportBug',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bugDes', models.CharField(max_length=5000)),
            ],
        ),
    ]
