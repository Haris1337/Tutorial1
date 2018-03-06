from django.conf.urls import url
from . import views

#different url patterns using the different methods
app_name = 'blog'

urlpatterns = [
	url(r'post$',views.post_list),
	url(r'add$',views.add, name='add'),
#	url(r'details/(?P<pk>[\w :-]+)/$', views.blog_detail, name="detail"),
	url(r'details/(?P<id>[0-9]+)/$', views.blog_detail, name="detail"),
	url(r'new_post/$', views.new_post, name="new_post"),
#	url(r'^comment/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
]
