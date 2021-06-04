from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='parentsPage'),
    url(r'^submissionParent', views.submissionsParent, name='submissionsParent'),
	url(r'^upload_file', views.subView, name='upload_file'),
	url(r'^success/', views.successView, name='success'),
	url(r'^(polls)/$', views.detail, name='detail'),
    url('Message/', views.MessageView, name='Message'),
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'^news', views.news, name='news'),
	url('bugReport/', views.reportBugView, name='reportBug'),
    url(r'^about', views.about, name='about'),
	url('kidInfo/', views.kidInfo, name='kidInfo'),
    url(r'^reviews/', views.reviews, name='reviews'),

]