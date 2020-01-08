from django.shortcuts import render
from django.contrib.auth.models import User
from retired.models import Profile
from .forms import SignupUpdate

def index(request, **kwargs):

	# user_profile = get_object_or_404(Profile, request.user)
	# user_added = User.objects.filter(id=kwargs.get('retire_id', "")).first()
	# if user_added in 
	# if request.method == 'POST':
	# 	a_form = SignupUpdate(request.POST)
	# 	if a_form.is_valid():
	# 		a_form.save()
	# 		messages.success(request, f'Your account hasbeen updated!')
	# 		return redirect('account')
	# else:
	# 	a_form = SignupUpdate()

	contex = {
	#	'a_form' : a_form,
		'users': User.objects.all()
	}

	return render(request, 'pools/home.html', contex)

def account(request):
	return render(request, 'pools/account.html')