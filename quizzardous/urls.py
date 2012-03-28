from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', 'quizzardous.questions.views.questions', name='questions'),
)

# only used in development environment (to serve static files)
urlpatterns += staticfiles_urlpatterns()
