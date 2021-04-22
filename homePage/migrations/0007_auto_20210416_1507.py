# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-04-16 12:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homePage', '0006_meeting'),
    ]

    operations = [
        migrations.RenameField(
            model_name='meeting',
            old_name='Meeting_text',
            new_name='Meeting_Link',
        ),
        migrations.AddField(
            model_name='meeting',
            name='date',
            field=models.CharField(default='Not determined', max_length=200),
            preserve_default=False,
        ),
    ]