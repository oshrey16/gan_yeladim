# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class myInfo(models.Model):
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    phoneNumber = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    birthDate = models.CharField(max_length=200)
    def __str__(self):
        return "My Information"
