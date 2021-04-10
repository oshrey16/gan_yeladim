from django.db import models

class submission(models.Model):
	kidId = models.CharField(max_length=200)
	subjectName = models.CharField(max_length=200)
	submissions = models.FileField(upload_to='submissionsTasksKids/')	
	def __str__(self):
		return self.kidId + self.subjectName