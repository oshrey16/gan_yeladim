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
	def __str__(self):
		return self.id + ":" + self.firstName + " " + self.lastName
	
class subject(models.Model):
	nameSubject = models.CharField(max_length=200, primary_key=True)
	songs = models.CharField(max_length=2000)
	selfTasks = models.CharField(max_length=2000)
	submissions = models.FileField(upload_to='submissionsTasks')	
	def __str__(self):
		return self.nameSubject
		
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