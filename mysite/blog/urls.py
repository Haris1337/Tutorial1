from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'post$',views.post_list),
	url(r'add$',views.add, name='add'),
]
