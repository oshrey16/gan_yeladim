from django.conf.urls import include, url
from django.contrib import admin
from homePage import views

urlpatterns = [
    url(r'^homePage/', views.login_success, name='login_success'),
    url(r'^ganenet/', admin.site.urls),
	url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^parentsPage/', include('parentsPage.urls')),
    url(r'^kidsPage/', include('kidsPage.urls')),
]