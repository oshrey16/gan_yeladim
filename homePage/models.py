from django.db import models
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.conf import settings
from django.db.models import (
    DateField, DateTimeField, DurationField, Field, IntegerField, TimeField,
    Transform,
)
from django.db.models.lookups import (
    YearExact, YearGt, YearGte, YearLt, YearLte,
)

import datetime
from django.db.models import DEFERRED

class kid(models.Model):
	id = models.CharField(max_length=200, primary_key=True)
	firstName = models.CharField(max_length=200)
	lastName = models.CharField(max_length=200)
	birth_date = models.DateTimeField('birthday')
	favoriteColor = models.CharField(max_length=200)
	favoriteAnimal = models.CharField(max_length=200)
	siblingsNumber = models.IntegerField(default=0)
	parentName = models.CharField(max_length=200)
	parentPhone = models.CharField(max_length=200)
	parentEmail = models.CharField(max_length=200)
	def __str__(self):
		return self.id + ":" + self.firstName + " " + self.lastName
		
class parent(models.Model):
	id = models.CharField(max_length=200, primary_key=True)
	firstName = models.CharField(max_length=200)
	lastName = models.CharField(max_length=200)
	kid = models.ForeignKey(kid, on_delete=models.CASCADE)
	birth_date = models.DateTimeField('birthday')
	parentPhone = models.CharField(max_length=200)
	parentEmail = models.CharField(max_length=200)
	def __str__(self):
		return self.firstName + " " + self.lastName + " ,Parent of: " +self.kid.id
		
class subject(models.Model):
	nameSubject = models.CharField(max_length=200, primary_key=True)
	songs = models.CharField(max_length=2000)
	selfTasks = models.CharField(max_length=2000)
	submissions = models.FileField(upload_to='submissionsTasks')	
	def __str__(self):
		return self.nameSubject
	
	def save(self, **kwargs):
		super(subject, self).save(**kwargs)
		mmashov = mashov(subject=self)
		mmashov.save()


# ================ #
# model Survey
# ================ #
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    def __str__(self):
        return self.question_text
    
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)	
    def __str__(self):
        return self.choice_text

class Meeting(models.Model):
    Meeting_Link = models.CharField(max_length=2000)
    date = models.CharField(max_length=200)
    def __str__(self):
        return self.Meeting_Link + "," + self.date 


# ================ #
# model News
# ================ #

class News(models.Model):
	ticket_id = models.AutoField(primary_key=True)
	title = models.CharField(max_length=200)
	content = models.TextField()
	ticket_date = models.DateTimeField(auto_now_add=True,auto_created=True)
	def __str__(self):
		return str(self.ticket_id) + "-" + self.title
		
		
class reportBug (models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    emailAddress = models.CharField(max_length=100)
    phoneNumber = models.CharField(max_length=15)
    subject = models.CharField(max_length=500)
    message = models.CharField(max_length=5000,blank=True)
    def __str__(self):
        return self.subject

class mashov (models.Model):
	subject = models.ForeignKey(subject,on_delete=models.CASCADE)
	feedback = models.IntegerField(default=0)
	v1 = models.IntegerField(default=0)
	v2 = models.IntegerField(default=0)
	v3 = models.IntegerField(default=0)
	v4 = models.IntegerField(default=0)
	v5 = models.IntegerField(default=0)
	def __str__(self):
		return self.subject.nameSubject

class Message (models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    emailAddress = models.CharField(max_length=100)
    phoneNumber = models.CharField(max_length=15)
    subject = models.CharField(max_length=500)
    message = models.CharField(max_length=5000,blank=True)
    def __str__(self):
        return self.subject

class trackinglog (models.Model):
	kid = models.ForeignKey(kid,on_delete=models.CASCADE)
	report_date = models.DateTimeField(auto_now_add=True,auto_created=True)
	message = models.CharField(max_length=5000,blank=True)
	def __str__(self):
		return 'report: ' + self.kid.firstName + ' ' + str(self.report_date.date())