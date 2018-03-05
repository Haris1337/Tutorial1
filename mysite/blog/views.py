from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import Post, Comments
from django.contrib.auth.decorators import login_required
from .forms import CommentForm

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

#Retrieved the post objects by its id
def blog_detail(request, id):
	blog = Post.objects.get(id=id)
	comments = Comments.objects.filter(post=blog)
	if request.method == 'POST':
		print 'request.POST', request.POST
	#Comment posted
		comment_form = CommentForm(data=request.POST)
		print '1'
		if comment_form.is_valid():
			print '2'
			#create comment obj
			new_comment = comment_form.save(commit=False)
			print '3'
			#assign post to comment
			new_comment.post = blog
			print '4'
			#save to db
#			new_comment.post_id=id #this works too.
			new_comment.save()
			print '5'
	else:
		comment_form = CommentForm()


	return render(request, 'blog/blog_detail.html', {'blog':blog, 'comments':comments, 'comment_form':comment_form})
