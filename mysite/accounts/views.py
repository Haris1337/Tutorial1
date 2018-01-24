from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect





def signup_view(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST) #Post data with the post request in to UCF
		if form.is_valid():
			user = form.save()
			user.backend = 'django.contrib.auth.backends.ModelBackend' #hackerboy
			login(request, user) #log the user in
			return redirect ('/post') #application blog, url post.
	else:
		form = UserCreationForm()
	
	return render(request, 'accounts/signup.html', {'form':form})

def login_view(request):
	if request.method == 'POST':
		form = AuthenticationForm(data=request.POST) #send this data into this form
		if form.is_valid():
			#log the user in
			user = form.get_user()
			login(request, user)
			#if 'next' in request.POST:
			#	return redirect(request.POST.get('next'))
			#else:
		return redirect('/post') #redirect to post

	else: 
		form = AuthenticationForm() #if not valid, will send to previous form and post errors
	
	return render(request, 'accounts/login.html', {'form':form})

def logout_view(request):
	if request.method == 'POST':
		logout(request)
		return redirect('/post')
	else:
		print request.user
		print request.method
		print "hello get"
		return redirect('/post')
		

