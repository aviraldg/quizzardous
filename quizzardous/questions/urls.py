from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('quizzardous.questions.views',
	url(r'^$', 'questions', name='questions'),
)
