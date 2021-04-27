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

class Submission(models.Model):
	nameSubmission= models.CharField(max_length=200, primary_key=True)
	
	def __str__(self):
		return self.nameSubmission
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