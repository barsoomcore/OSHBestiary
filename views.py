from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.views.generic import create_update

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from tagging.models import Tag, TaggedItem

from dponisetting.dponiwiki.forms import UserCreationFormExtended
from oshbestiary.models import Creature
from oshbestiary.forms import CreatureForm

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

    
def register(request):
	
	if request.method == 'POST':
		form = UserCreationFormExtended(data=request.POST)
		if form.is_valid():
			new_user = form.save()			
			user = authenticate(username=new_user.username, password=form.cleaned_data['password1'])
			if user is not None:
				login(request, user)
			return HttpResponseRedirect(reverse('osh_index'))
	else: form = UserCreationFormExtended()
		
	return render_to_response(
		'templates/registration/osh_registration_form.html', 
		{ 'form' : form }, 
		context_instance=RequestContext(request)
	)

@login_required
def update_creature(request, slug=None):
	try:
		creature = Creature.objects.get(slug__exact=slug)
		owner = creature.owner
	except Creature.DoesNotExist:
		creature = None
		
	if request.method == 'POST':
		form = CreatureForm(request.POST, instance=creature)
		if form.is_valid():
			creature = form.save(commit=False)
			if slug == None:
				owner = request.user
			creature.save(owner=owner)
			return HttpResponseRedirect(creature.get_absolute_url())
	
	else:
		if creature:
			form = CreatureForm(instance=creature)
		else:
			form = CreatureForm(instance=creature, initial={'owner':request.user})
		
	return render_to_response(
		'templates/creature_form.html', 
		locals(), 
		context_instance=RequestContext(request)
	)