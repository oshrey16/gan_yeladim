from django import forms
from django.forms import ModelForm
from parentsPage.models import submission
from parentsPage.models import 
from homePage.models import reportBug

class subForm(ModelForm):
    submissions = forms.FileField
    class Meta:
        model = submission
        fields = ['kidId', 'subjectName','submissions']
		
class ContactForm(forms.ModelForm):
    class Meta:
        model = reportBug
        fields = ['firstName', 'lastName','emailAddress','phoneNumber','subject','message']		
