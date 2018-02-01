from django.conf.urls import url
from . import views

#different url patterns using the different methods
app_name = 'blog'

urlpatterns = [
	url(r'post$',views.post_list),
	url(r'add$',views.add, name='add'),
	url(r'^(?P<title>[\w-]+)/$', views.blog_detail, name="detail"),
]
