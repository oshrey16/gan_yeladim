from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^viewSubmission', views.viewSubmission, name='view subjects'),
    url(r'^subject/(?P<subjectName>[a-zA-Z]+)/$', views.Submissions, name='view submission'),
    url(r'^subject/(?P<subjectName>[a-zA-Z]+)/$', views.add_review, name='Review'),
    #url(r'^reviewGanenet', views.reviewGanenet, name='Review'),
	url(r'^addReview', views.add_review, name='add a Review'),
    url(r'^reviewGanenet', views.reviewGanenet, name='reviewGanenet'),
    url(r'^success/', views.successView, name='success'),
    url(r'^viewmashovs/$', views.viewmashovs, name='viewmashovs'),
]