from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('questions.views',
    url(r'^$', 'questions', name='questions'),
)
