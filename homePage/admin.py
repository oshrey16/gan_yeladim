from django.contrib import admin

from .models import kid, subject, Question, Choice,Meeting,News,Submission


admin.site.register(kid)
admin.site.register(subject)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Submission)
admin.site.register(Meeting)
admin.site.register(News)
