from django.db import models
from django.db.models import permalink
from django.contrib import admin
from django.contrib.auth.models import User

from tagging.fields import TagField
from tagging.models import Tag
from autoslug.fields import AutoSlugField

class Power(models.Model):
	name = models.CharField(max_length=100)
	slug = AutoSlugField(populate_from='name', unique=True, editable=False)
	owner = models.ForeignKey(User)
	description = models.TextField()
	tags = TagField(blank=True)
	
	POWER_TYPES = (
		('Constant', 'Constant'),
		('Per-Arena', 'Per-Arena'),
		('Rested', 'Rested'),
	)
	
	type = models.CharField(blank=True, max_length=20, choices=POWER_TYPES)
	focused = models.BooleanField()
	
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)
	
	class Meta:
		ordering = ['name']
	
	@permalink
	def get_absolute_url(self):
		return('power-detail', (), {'slug': self.slug})
	
	def __unicode__(self):
		return u'%s' % (self.name)

class Creature(models.Model):
	name = models.CharField(max_length=100)
	slug = AutoSlugField(populate_from='name', unique=True, editable=False)
	owner = models.ForeignKey(User)
	description = models.TextField()
	tags = TagField(blank=True)
	
	WEAPON_CHOICES = (
		('Light', 'Light'),
		('Heavy', 'Heavy'),
		('Reach', 'Reach'),
		('Ranged', 'Ranged'),
		('Very Heavy', 'Very Heavy'),
	)
	AC = models.IntegerField()
	hit_points = models.IntegerField()
	brawn = models.IntegerField(blank=True, null=True)
	cunning = models.IntegerField(blank=True, null=True)
	daring = models.IntegerField(blank=True, null=True)
	charm = models.IntegerField(blank=True, null=True)
	commitment = models.IntegerField(blank=True, null=True)
	awareness = models.IntegerField(blank=True, null=True)
	weapon = models.CharField(blank=True, max_length=20, choices=WEAPON_CHOICES)
	
	powers = models.ManyToManyField(
		'Power', 
		related_name='creatures_used',
		blank=True
	)
	
	image = models.URLField(blank=True)
	
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)
	
	@permalink
	def get_absolute_url(self):
		return('osh-creature-detail', (), {'slug': self.slug})
	
	def __unicode__(self):
		return u'%s' % (self.name)
	