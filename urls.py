from django.conf.urls.defaults import *

from oshbestiary.models import Power, Creature

urlpatterns = patterns('django.views.generic',
    url(r'^$', 'simple.direct_to_template', { 'template': 'oshbestiary_index.html'}),
    url(r'^(?P<slug>[-\w]+)/$', 'list_detail.object_detail', 
    {
    	'queryset': Creature.objects.all(), 
    	'template_name': 'creature_detail.html'
    }, name='creature-detail'
    ),
)