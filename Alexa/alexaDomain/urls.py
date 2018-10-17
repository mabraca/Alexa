from django.conf.urls import url
from . import views 


urlpatterns = [
	url(
	        '',
	        views.Domain.as_view(),
	         name="Alexa's Domain"
	    ),
]