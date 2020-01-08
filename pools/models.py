from django.db import models
from django.contrib.auth.models import User
from retired.models import Profile

class Account(models.Model):
	user = models.ForeignKey(Profile, on_delete = models.SET_NULL, null=True)
	adduser = models.OneToOneField(User, on_delete = models.SET_NULL, null = True)
	approve = models.BooleanField(default=False) 

	def get_account_added(self):
		return self.adduser.all()
