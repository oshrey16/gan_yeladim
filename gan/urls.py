from django.conf.urls import include, url
from django.contrib import admin
from homePage import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^homePage/', views.login_success, name='login_success'),
    url(r'^ganenet/', admin.site.urls),
	url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^parentsPage/', include('parentsPage.urls')),
    url(r'^kidsPage/', include('kidsPage.urls')),
    url(r'^ganenetPage/', include('ganenetPage.urls')),
]

urlpatterns += staticfiles_urlpatterns()