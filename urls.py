from django.conf.urls.defaults import *

from oshbestiary.models import Power, Creature

extra_context_blurb = {'blurb': True}

urlpatterns = patterns('django.views.generic.list_detail',
    url(r'^$', 'object_list', { 
    	'queryset': Creature.objects.all(), 
    	'template_name': 'oshbestiary_index.html',
    	'template_object_name': 'creature',
    	'extra_context': extra_context_blurb},
    	name='osh-index'
    ),
    url(r'^(?P<slug>[-\w]+)/$', 'object_detail', 
    {
    	'queryset': Creature.objects.all(), 
    	'template_name': 'creature_detail.html'
    }, name='osh-creature-detail'
    ),
)

urlpatterns += patterns('oshbestiary.views',
	url(r'^tag/(?P<tag>.*)/$', 'by_tag', name='osh-by-tag'),
)