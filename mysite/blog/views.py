from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Post
from django.contrib.auth.decorators import login_required

#Prints the 10 first objects in the list
def post_list(request):
	posts = Post.objects.all()[:10]

	context = {
		'posts':posts
	}

	return render(request, 'blog/base2.html', context)


#adds a new object to the list using title, author and body
@login_required(login_url="/accounts/login")
def add(request):

	if(request.method == 'POST'):
		print "request.POST", request.POST
		title = request.POST['title']
		author = request.POST['author']
		body = request.POST['body']
		u = User.objects.get(id=int(author))			
		post = Post(title=title, author=u, body=body)
		post.save()

		return redirect('/post')
	else:
		users = User.objects.all()
		user = {
		      'users':users
		}

		return render(request, 'blog/add.html', user)

def blog_detail(request, title):
	blog = Post.objects.get(title=title)
	return render(request, 'blog/blog_detail.html', {'blog':blog})	


