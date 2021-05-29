from django.conf.urls import url
from . import views
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    url(r'^$', views.index, name='kidsPage'),
	url(r'^(Meetings)/$', views.meetings, name='meetings'),
	url(r'^(subject)/$', views.contents, name='contents'),
	url(r'^(?P<fl_path>[a-zA-Z]+)/', views.download_file),
	url(r'^(?P<mashov_id>[0-9]+)/vote/$', views.vote, name='vote'),
]