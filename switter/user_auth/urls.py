from django.conf.urls import patterns, include, url
urlpatterns = patterns('',
	url(r'^signout$', 'user_auth.views.signout', name='signout'),
	url(r'^signup$', 'user_auth.views.signup', name='signup'),
	url(r'^profile$', 'user_auth.views.profile', name='profile'),
	url(r'^', 'user_auth.views.signin',name='signin'),
	
	
)