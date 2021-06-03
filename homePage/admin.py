from django.contrib import admin

from .models import kid, parent, subject, Question, Choice,Meeting,News,mashov,trackinglog
from parentsPage.models import submission

admin.site.register(kid)
admin.site.register(parent)
admin.site.register(subject)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(submission)
admin.site.register(Meeting)
admin.site.register(News)
admin.site.register(mashov)
admin.site.register(trackinglog)
