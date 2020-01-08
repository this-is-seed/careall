from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm, ProfileUpdateForm, ProfileUpdateFormH


@login_required
def profile(request):
	if request.user.groups.filter(name='retired').exists():
		if request.method == 'POST':
			u_form = UserUpdateForm(request.POST, instance = request.user)
			p_form = ProfileUpdateForm(request.POST, request.FILES, instance = request.user.profile)
			if u_form.is_valid() and p_form.is_valid():
				u_form.save()
				p_form.save()
				messages.success(request, f'Your account hasbeen updated!')
				return redirect('profile')


		else:
			u_form = UserUpdateForm(instance = request.user)
			p_form = ProfileUpdateForm(instance = request.user.profile)

		contex = {
			'u_form' : u_form,
			'p_form' : p_form
		}

		return render(request, 'retired/profile.html', contex)

	else:
		if request.method == 'POST':
			u_form = UserUpdateForm(request.POST, instance = request.user)
			p_form = ProfileUpdateFormH(request.POST, request.FILES, instance = request.user.profile)
			if u_form.is_valid() and p_form.is_valid():
				u_form.save()
				p_form.save()
				messages.success(request, f'Your account hasbeen updated!')
				return redirect('profile')


		else:
			u_form = UserUpdateForm(instance = request.user)
			p_form = ProfileUpdateFormH(instance = request.user.profile)

		contex = {
			'u_form' : u_form,
			'p_form' : p_form
		}

		return render(request, 'retired/profile.html', contex)





