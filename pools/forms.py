from django import forms
from django.contrib.auth.models import User
from .models import Account

class SignupUpdate(forms.ModelForm):
	pass
	# class Meta:
	# 	model = Account
	# 	fields = ['retired_id', 'approve']