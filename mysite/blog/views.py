from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import Post, Comments
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .forms import CommentForm, PostForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



def post_list(request):
	queryset_list = Post.objects.all()
	#Request input field and filter the post_list by title contents
	query = request.GET.get('q')
	print "query: ", query
	if query:
		queryset_list = queryset_list.filter(
		Q(title__icontains=query) #|
		#Q(body__icontains=query)
		).distinct()
	#Filter by body
	query1 = request.GET.get('s')
	print "query1: ", query1
	if query1:
		queryset_list = queryset_list.filter(
		Q(body__icontains=query1)
		).distinct()
	#filter by publish date
	query2 = request.GET.get('q1')
	print "query2: ", query2
	if query2:
		queryset_list = queryset_list.filter(
		Q(publish__icontains=query2)
		).distinct()


	paginator = Paginator(queryset_list, 5) #Show 5 posts per page

	page = request.GET.get('page')
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		queryset = paginator.page(1)
	except EmptyPage:
		queryset = paginator.page(paginator.num_pages)


	context = {
		'object_list':queryset
	}

	print request.GET.get('q')
	print request.GET.get('q1')
	print request.GET.get('s')


	return render(request, 'blog/base2.html', context)


#adds a new object to the list using title, author and body
@login_required(login_url="/accounts/login")
def add(request):
	if(request.method == 'POST'):
		print "request.POST", request.POST
		title = request.POST['title']
		author = request.user.get_username()
		body = request.POST['body']
		u = User.objects.get(username=author)
		post = Post(title=title, author=u, body=body)
		post.save()

		return redirect('/')
	else:
		users = User.objects.all()
		user = {
		      'users':users
		}

		return render(request, 'blog/add.html', user)

@login_required(login_url="/accounts/login")
def post_new(request):
	form = PostForm(request.POST)
	if form.is_valid():
		post = form.save(commit=False)
		post.author = request.user
		post.save()
		return redirect('/')
	else:
		form = PostForm()
	return render (request, 'blog/edit_post.html', {'form':form})

def post_edit(request, id):
	post =  Post.objects.get(id=id) #get_object_or_404(Post, id=id)
	print post
	if (request.method == 'POST'):
		form = PostForm(request.POST, instance=post)
		if form.is_valid():
			post = form.save(commit=False)
			post.edited = True
			post.author = request.user
			post.save()
			return redirect('/')
	else:
		form = PostForm(instance=post)
	return render (request, 'blog/edit_post.html', {'form':form})

#Retrieved the post objects by its id
def blog_detail(request, id):
	blog = Post.objects.get(id=id)
	comments = Comments.objects.filter(post=blog)
	if request.method == 'POST':
		print 'request.POST', request.POST
	#Comment posted
		comment_form = CommentForm(data=request.POST)
		if comment_form.is_valid():
			#create comment obj
			new_comment = comment_form.save(commit=False)
			#assign post to comment
			new_comment.post = blog
			#save to db
#			new_comment.post_id=id #this works too.
			new_comment.save()
	else:
		comment_form = CommentForm()


	return render(request, 'blog/blog_detail.html', {'blog':blog, 'comments':comments, 'comment_form':comment_form})
