from django.conf.urls import url
from . import views

#different url patterns using the different methods
urlpatterns = [
	url(r'post$',views.post_list),
	url(r'add$',views.add, name='add'),
]
