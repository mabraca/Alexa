from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', )
		


class URLForm(forms.Form):
    nameURL = forms.URLField(label='URL', max_length=100)