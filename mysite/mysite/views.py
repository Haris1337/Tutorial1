from django.shortcuts import render_to_response #allows us to render a template to browser
from django.http import HttpResponseRedirect #allows us to redirect browser to urls
from django.contrib import auth #takes care of user/pw and login session
from django.core.context_processors import csrf #Token to secure site

#Passing through csrf token to login.html
def login(request):
	c ={}
	c.update(csrf(request))
	return render_to_response('login.html', c)

def auth_view(request):
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	#main check - if it finds a match, it will return a user obj else none.
	user = auth.authenticate(username=username, password=password)
	
	if user is not None:
		auth.login(request, user)
		return HttpResponseRedirect('/accounts/loggedin')
	else
		return HttpResponseRedirect('/accounts/invalid_login')

def loggedin(request):
	return render_to_response('loggedin.html', {'username': request.user.username})

def invalid_login(request):
	return render_to_response('invalid_login.html')

def logout(request):
	auth.logout(request)
	return render_to_response('logout.html')
