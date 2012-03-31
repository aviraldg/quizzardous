from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('users.views',
    url(r'^(?P<pk>\d+)$', 'user_profile', name='user_profile'),
)
