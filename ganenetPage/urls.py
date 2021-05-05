from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^viewSubmission', views.viewSubmission, name='view subjects'),
    url(r'^subject/(?P<subjectName>[a-zA-Z]+)/$', views.Submissions, name='view submission'),
]