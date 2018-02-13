from django.contrib.auth.models import User
from django import forms
from .models import Post, Comments

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comments
		fields = ['comment_text',]

