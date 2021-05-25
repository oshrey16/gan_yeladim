from django import forms
from django.forms import ModelForm
from parentsPage.models import submission
from parentsPage.models import 
from homePage.models import reportBug
from homePage.models import Message



class subForm(ModelForm):
    submissions = forms.FileField
    class Meta:
        model = submission
        fields = ['kidId', 'subjectName','submissions']
		
class ContactForm(forms.ModelForm):
    class Meta:
        model = reportBug
<<<<<<< HEAD
        fields = ['firstName', 'lastName','emailAddress','phoneNumber','subject','message']	

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['firstName', 'lastName','emailAddress','phoneNumber','subject','message']	


=======
        fields = ['firstName', 'lastName','emailAddress','phoneNumber','subject','message']		
>>>>>>> af20a0a2753f0589dc993a9415b3cbdaa179fad2
