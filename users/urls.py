from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
    (r'^login/$', 'django.contrib.auth.views.login', {
        'template_name': 'users/login.html',
    }, 'login'),

    (r'^logout/$',
        'django.contrib.auth.views.logout_then_login',
        {},
        'logout'),

    url(r'^(?P<pk>\d+)/(?P<username>\S+)/$',
        'users.views.user_profile',
        name='user_profile'),
)
