from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate
from .forms import UserLoginForm





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
	form = UserLoginForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get("username") #Form subclass, cleanes the specific form attribute.
		password = form.cleaned_data.get("password") #does not pass parameters. Looks up value in form.
		user = authenticate(username=username, password=password) #request the object with UN/PW == UN/PW. Checks the DB for UN/PW.
		if user is not None: #if the user exists, request the user and use imported login function.
			login(request, user) # ^
		return redirect('/post') #if logged in, redirect to /post
	else:
		form = UserLoginForm()
	return render(request, 'accounts/login.html', {'form':form})
'''

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
'''

def logout_view(request): #builtin logout for function
	if request.method == 'POST':
		logout(request)
		return redirect('/post')
	else:
		print request.user
		print request.method
		print "hello get"
		return redirect('/post')
		

