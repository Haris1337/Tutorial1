from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
# Create your models here.
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible  # only if you need to support Python 2
class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    edited = models.BooleanField(default=False)

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title


class Comments(models.Model):
	comment_text = models.CharField(max_length=200)
	time_of_comment = models.DateTimeField(default=timezone.now)
	post = models.ForeignKey(Post, related_name='blog_comments')
# 	user = models.ForeignKey(User)

	def __str__(self):
		return self.comment_text
