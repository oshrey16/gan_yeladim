from django.conf.urls import include, url
from django.contrib import admin
from homePage import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import logout

urlpatterns = [
    url(r'^homePage/', views.login_success, name='login_success'),
    url(r'^ganenet/', admin.site.urls),
	url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^parentsPage/', include('parentsPage.urls')),
    url(r'^kidsPage/', include('kidsPage.urls')),
    url(r'^ganenetPage/', include('ganenetPage.urls')),
    url(r'about', views.about),
    url(r'home', views.home),
    url(r'^logout/$', logout, {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
    url(r'zorkesher', views.zorkesher),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)