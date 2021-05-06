from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
   review = forms.FileField
   class Meta:
        model = Review
        fields = ['review','submission_id']