from django import forms
from django.contrib.auth import (authenticate, get_user_model,)

User = get_user_model()

class UserLoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)

	def clean(self): #*args lets u pass non-keyword variable length argument list to a function. **kwargs does keyworded.
					 #Clean method on a Field subclass is responsible for running to_python(), validate() &  run_validators() in correct order, and propagate their errors.
		username = self.cleaned_data.get("username")
		password = self.cleaned_data.get("password")
		user = authenticate(username=username, password=password)
		print '1'
		if not user:
			raise forms.ValidationError("user does not exist")  #If, at any time, any of the methods raise ValidationError, the validation stops and that error is raised

		print '2'
		if not user.check_password(password):
			raise forms.ValidationError("password does not match")
		print '3'
		if not user.is_active:
			raise forms.ValidationError("account nolonger is active")
		return super(UserLoginForm, self).clean() #return the default
