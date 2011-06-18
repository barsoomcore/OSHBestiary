from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from models import Creature

class CreatureForm(forms.ModelForm):
	name = forms.CharField(label='Name (Required)')
	description = forms.CharField(widget=forms.Textarea, label='Description (Required)')
	AC = forms.IntegerField(label='AC (Required)', error_messages={'required': '*'})
	hit_points = forms.IntegerField(label='Hit Points (Required)', error_messages={'required': '*'})
	
	class Meta:
		model = Creature

class UserCreationFormExtended(UserCreationForm):

	def __init__(self, *args, **kwargs):
		super(UserCreationFormExtended, self).__init__(*args, **kwargs)
		self.fields['email'].required = True

	class Meta:
		model = User
		fields = ('username', 'email')