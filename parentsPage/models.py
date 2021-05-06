from django.db import models
from homePage.models import kid,subject

class submission(models.Model):
	kidId = models.ForeignKey(kid,on_delete=models.CASCADE)
	subjectName = models.ForeignKey(subject,on_delete=models.CASCADE)
	
	submissions = models.FileField(upload_to='submissionsTasksKids/')	

	def __str__(self):
		return self.kidId.id + self.subjectName.nameSubject