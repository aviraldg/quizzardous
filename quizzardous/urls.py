from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic.simple import redirect_to
from django.core.urlresolvers import reverse

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # TODO: This, the homepage, should in the future point to a list of the
    # most popular recent questions. For now, this should do.
    (r'^$', redirect_to, {'url': 'questions'}),
    (r'^questions/', include('questions.urls')),
    (r'^users/', include('users.urls'))
)

# only used in development environment (to serve static files)
urlpatterns += staticfiles_urlpatterns()
