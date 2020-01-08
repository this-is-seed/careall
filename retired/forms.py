from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.forms import UserCreationForm


class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
	
	class Meta:
		model = Profile
		fields = ['image', 'help']

class ProfileUpdateFormH(forms.ModelForm):
	
	class Meta:
		model = Profile
		fields = ['image']

