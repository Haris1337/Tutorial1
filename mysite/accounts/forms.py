from django import forms
from django.contrib.auth import (authenticate, get_user_model,)

User = get_user_model()

class UserLoginForm(forms.Form):
	username = forms.CharField()
	password.CharField(widget=forms.PasswordInput)

	def clean(self, *args, **kwargs): #*args lets u pass non-keyword variable length argument list to a function. 										  **kwargs does keyworded.
		username = self.cleaned_data.get("username")
		password = self.cleaned_data.get("password")
		user = authenticate(username=username, password=password)
		if not user:
			raise forms.ValidationErrors("user does not exist")

		
		if not user.check_password(password):
			raise forms.ValidationError("password does not match")

		if not user.is_active:
			raise forms.ValidationError("account nolonger exist")
		return super(UserLoginForm, self).clean
