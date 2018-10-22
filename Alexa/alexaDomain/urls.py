from django.conf.urls import url
from . import views 
from django.contrib.auth import views as auth_views



urlpatterns = [
	
	url(r'^login/$', 
		auth_views.login,
		{'template_name': 'registration/login.html'}, 
		name="login"
	),

	url(r'^logout/$', 
		auth_views.logout, 
		{'next_page': '/login/'},
		name="logout"
	),

	url("register/", 
		views.Register.as_view(), 
		name="register"
	),
	url('',
	    views.Domain.as_view(),
	     name="Alexa's Domain"
	 ),
]