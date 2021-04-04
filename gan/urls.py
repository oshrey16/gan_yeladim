from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^homePage/', include('homePage.urls')),
    url(r'^ganenet/', admin.site.urls),
	url(r'^accounts/', include('django.contrib.auth.urls')),
]