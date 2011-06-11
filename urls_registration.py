from django.conf.urls.defaults import *
from django.contrib.auth.views import login

urlpatterns = patterns('django.contrib.auth.views',
    url(r'^login/$',  
    	'login', 
    	{ 'template_name': 'templates/registration/osh_login.html'}, 
    	name='osh_login'
    ),
    url(r'^logout/$', 
    	'logout', 
    	{'next_page': '/'}, 
    	name='osh_logout'
    ),
	url(r'^password_change/$', 
		'password_change', 
		{'template_name': 'templates/registration/osh_password_change_form.html'}, 
		name='osh_password_change'
	),
	url(r'^password_change/done/$', 
		'password_change_done', 
		{'template_name': 'templates/registration/osh_password_change_done.html'}
	),
	url(r'^password_reset/$',
		'password_reset',
		{'template_name': 'templates/registration/osh_password_reset_form.html',
		'email_template_name': 'templates/registration/osh_password_reset_email.html'},
		name='osh_password_reset'
	),
	url(r'^password_reset/done/$',
		'password_reset_done',
		{'template_name': 'templates/registration/osh_password_reset_done.html'},
		name='osh_password_reset_done'
	),
	url(r'^password_reset_confirm/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$',
		'password_reset_confirm',
		{'template_name': 'templates/registration/osh_password_reset_confirm.html'},
		name='osh_password_reset_confirm'
	),
	url(r'^password_reset_complete/$',
		'password_reset_complete',
		{'template_name': 'templates/registration/osh_password_reset_complete.html'},
		name='osh_password_reset_complete'
	),
)

urlpatterns += patterns('oshbestiary.views',
	url(r'register/$', 'register', name='osh_register'),
)