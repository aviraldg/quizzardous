from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('rankings.views',
    url(r'^$', 'rankings', name='rankings'),
)
