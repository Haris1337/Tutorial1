from django.shortcuts import render, redirect
from .models import Post

def post_list(request):
	posts = Post.objects.all()[:10]

	context = {
		'posts':posts
	}

	return render(request, 'blog/base2.html', context)


def add(request):
	if(request.method == 'POST'):
		title = request.POST['title']
		author = request.POST['author']
		body = request.POST['body']
		
		post = Post(title=title, author=author, body=body)
		post.save()

		return redirect('/posts')
	else:
		return render(request, 'blog/add.html')


