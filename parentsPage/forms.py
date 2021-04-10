from django import forms
from django.forms import ModelForm
from parentsPage.models import submission

class subForm(ModelForm):
    submissions = forms.FileField
    class Meta:
        model = submission
        fields = ['kidId', 'subjectName','submissions']