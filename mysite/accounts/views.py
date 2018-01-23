from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth.models import User


def signup_view(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST) #Post data with the post request in to UCF
		if form.is_valid():
			user = form.save()
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
			return redirect('/post') #redirect to post

	else: 
		form = AuthenticationForm() #if not valid, will send to previous form and post errors
	
	return render(request, 'accounts/login.html', {'form':form})

