from django.conf.urls import patterns, include, url
urlpatterns = patterns('',
	url(r'^$', 'blog.views.mainpage',name='mainpage'),
	url(r'^category/(?P<category_id>\d+)$', 'blog.views.by_category', name='by_category'),
	url(r'^post_info/(?P<post_id>\d+)$', 'blog.views.post_info', name='post_info'),
)