from django import forms
from django.forms import ModelForm
from parentsPage.models import submission
from homePage.models import reportBug, kid
from homePage.models import Message



class subForm(ModelForm):
    submissions = forms.FileField
    class Meta:
        model = submission
        fields = ['kidId', 'subjectName','submissions']
		
class ContactForm(forms.ModelForm):
    class Meta:
        model = reportBug
        fields = ['firstName', 'lastName','emailAddress','phoneNumber','subject','message']	

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['firstName', 'lastName','emailAddress','phoneNumber','subject','message']	

class KidForm(forms.ModelForm):
    class Meta:
        model = kid
        fields = ['id','firstName', 'lastName','birth_date','favoriteColor','favoriteAnimal','siblingsNumber','parentName','parentPhone','parentEmail']	
