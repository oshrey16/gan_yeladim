# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-05-06 17:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ganenetPage', '0002_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='Save',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result_text', models.CharField(max_length=200)),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ganenetPage.Review')),
            ],
        ),
    ]
