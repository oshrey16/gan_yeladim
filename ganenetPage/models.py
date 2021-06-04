# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from homePage.models import kid,subject
from django.db import models
from parentsPage.models import submission

# Create your models here.
class myInfo(models.Model):
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    phoneNumber = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    birthDate = models.DateTimeField('birthday')
    def __str__(self):
        return "My Information"

class Review(models.Model):
    review= models.TextField(max_length=1000)
    subjectName=models.ForeignKey(subject,on_delete=models.DO_NOTHING)
    submission_id=models.CharField(default=0,max_length=50)
    kidId=models.CharField(max_length=200, primary_key=True)

    def __str__(self):
        return self.review

# class Save(models.Model):
#     review = models.ForeignKey(Review, on_delete=models.CASCADE)
#     result_text = models.TextField (review)
#     def __str__(self):
#         return self.result_text