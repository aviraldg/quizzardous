from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('questions.views',
    url(r'^$', 'questions', name='questions'),
    url(r'^page/(?P<page>\d+)/$', 'questions'),
    url(r'^(?P<pk>\d+)/(?P<slug>\S+)/$', 'question', name='question'),
)
