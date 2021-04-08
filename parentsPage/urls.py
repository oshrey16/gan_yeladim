from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='parentsPage'),
    url(r'^submissionParent', views.submissionsParent, name='submissionsParent'),
]