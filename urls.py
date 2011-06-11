from django.conf.urls.defaults import *

from oshbestiary.models import Power, Creature

extra_context_blurb = {'blurb': True}

urlpatterns = patterns('',
	url(r'^accounts/', include('dponisetting.oshbestiary.urls_registration')),
)

urlpatterns += patterns('oshbestiary.views',
	url(r'^tag/(?P<tag>.*)/$', 'by_tag', name='osh-by-tag'),
	url(r'^create-creature/$', 'update_creature', name='create_creature'),
	url(r'^update-creature/(?P<slug>[-\w]+)/$', 'update_creature', name='update_creature'),
)

urlpatterns += patterns('django.views.generic.list_detail',
    url(r'^$', 'object_list', { 
    	'queryset': Creature.objects.all(), 
    	'template_name': 'oshbestiary_index.html',
    	'template_object_name': 'creature',
    	'extra_context': extra_context_blurb},
    	name='osh-index'
    ),
    url(r'^creature/(?P<slug>[-\w]+)/$', 'object_detail', 
    {
    	'queryset': Creature.objects.all(), 
    	'template_name': 'creature_detail.html'
    }, name='osh-creature-detail'
    ),
)