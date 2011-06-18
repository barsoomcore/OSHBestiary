from oshbestiary.models import Power, Creature
from django.contrib import admin

class PowerAdmin(admin.ModelAdmin):
	list_display = ('name', 'owner', 'description', 'type', 'tags', 'focused')
	
	def save_model(self, request, obj, form, change):
		obj.owner = request.user
		obj.save()

class CreatureAdmin(admin.ModelAdmin):
	list_display = ('name', 'owner', 'description', 'tags')
	
	def save_model(self, request, obj, form, change):
		obj.owner = request.user
		obj.save()

admin.site.register(Power, PowerAdmin)
admin.site.register(Creature, CreatureAdmin)