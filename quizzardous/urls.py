from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', 'quizzardous.qzds.views.questions', name='questions')
    # Examples:
    # url(r'^$', 'quizzardous.views.home', name='home'),
    # url(r'^quizzardous/', include('quizzardous.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

# only used in development environment
urlpatterns += staticfiles_urlpatterns()
