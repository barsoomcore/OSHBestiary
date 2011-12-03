from oshbestiary.models import Power, Creature
from django.contrib import admin

class PowerAdmin(admin.ModelAdmin):
	list_display = ('name', 'owner', 'description', 'type', 'tags', 'focused')
	
	def save_model(self, request, obj, form, change):
		obj.owner = request.user
		obj.save()

class CreatureAdmin(admin.ModelAdmin):
	list_display = ('name', 'owner', 'description', 'tags', 'public_link')
	
	def save_model(self, request, obj, form, change):
		obj.owner = request.user
		obj.save()
	
	def public_link(self, obj):
		return ("<a href='" + obj.get_absolute_url() + "'>View</a>")
	public_link.short_description=""
	public_link.allow_tags = True

admin.site.register(Power, PowerAdmin)
admin.site.register(Creature, CreatureAdmin)