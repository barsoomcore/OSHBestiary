from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from tagging.models import Tag, TaggedItem
from oshbestiary.models import Creature

def by_tag(request, tag):
	tag = get_object_or_404(Tag, name=tag)
	tagged_items = TaggedItem.objects.get_by_model(Creature, tag)
	
	template_params = {
		'tagged_items': tagged_items,
		'tag': tag
	}
	
	return render_to_response(
		'templates/creature_list.html',
		template_params,
		context_instance=(RequestContext(request))
	)