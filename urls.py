from django.conf.urls.defaults import *

from oshbestiary.models import Power, Creature

urlpatterns = patterns('django.views.generic.list_detail',
    url(r'^$', 'object_list', { 
    	'queryset': Creature.objects.all(), 
    	'template_name': 'oshbestiary_index.html',
    	'template_object_name': 'creature'}),
    url(r'^(?P<slug>[-\w]+)/$', 'object_detail', 
    {
    	'queryset': Creature.objects.all(), 
    	'template_name': 'creature_detail.html'
    }, name='creature-detail'
    ),
)