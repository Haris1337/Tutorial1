from django.contrib.auth.models import User
from django import forms
from .models import Post, Comments

#class CommentForm(forms.ModelForm):
#	class Meta:
#		model = models.Comments
#		fields = ['comment_text', 'time_of_comment']
