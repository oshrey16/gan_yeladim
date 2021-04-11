from django.contrib import admin

from .models import kid, subject
from parentsPage.models import submission

admin.site.register(kid)
admin.site.register(subject)
admin.site.register(submission)
