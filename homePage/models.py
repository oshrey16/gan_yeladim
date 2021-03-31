from django.db import models


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
	