
from django.conf.urls import url

import homePage
from . import views
from django.conf import settings
from django.views.static import serve
from django.conf.urls import include


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^viewSubmission', views.viewSubmission, name='view subjects'),
    url(r'^subject/(?P<subjectName>[a-zA-Z]+)/$', views.Submissions, name='view submission'),
    url(r'^subject/(?P<subjectName>[a-zA-Z]+)/$', views.add_review, name='Review'),
    #url(r'^reviewGanenet', views.reviewGanenet, name='Review'),
	url(r'^addReview', views.add_review, name='add a Review'),
    url(r'^reviewGanenet', views.reviewGanenet, name='reviewGanenet'),
    url(r'^success/', views.successView, name='success'),
    url(r'^viewmashovs/$', views.viewmashovs , name='viewmashovs'),
    url(r'^viewmashovss/$', views.viewmashovss , name='viewmashovss'),
    url(r'^about', homePage.views.about , name='about'),
    url(r'^trackinglog/$', views.trackinglog , name='trackinglog'),
]