from django.contrib import admin

from .models import kid, subject, Question, Choice,Meeting
from parentsPage.models import submission

admin.site.register(kid)
admin.site.register(subject)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(submission)
admin.site.register(Meeting)
