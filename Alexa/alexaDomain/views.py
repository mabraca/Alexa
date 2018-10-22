from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from django.shortcuts import render
from bs4 import BeautifulSoup
from urllib.request import urlopen
from django.template import RequestContext
from .forms import *
from .models import *
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
#Using UserModels Django
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin


class Register(TemplateView):
	# Register page
	template_view = "registration/register.html"

	def get(self, request, *args, **kwargs):
		form = UserRegistrationForm()
		#Return registration page
		return render(request, 'registration/register.html', {'form' : form})

	def post(self, request,*args, **kwargs):
		#Save de registration if all inputs are correct
		form = UserRegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			#Get the input information
			username = form.cleaned_data.get('username')
			passwordUser = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=passwordUser)
			login(request, user)
			return redirect('/')
		else:
			#Return errors if has it
			print(form.errors)
		return render(request, 'registration/register.html', {'form' : form})

		

class Domain(LoginRequiredMixin,TemplateView):
	# Main page
	template_view = "alexaDomain.html"
	login_url = '/login/'

	def get(self, request, *args, **kwargs):
		# Array of distionaries. It will return the result to the view
		dictDomains=[]

		#If database is empty then it will show the main Alexa's page 
		#If not is empty then look for the last url inserted in DB
		pageHead= recentViews.objects
		if(pageHead.count() < 1):
			lastPage='https://www.alexa.com/topsites'
		else:
			lastPage= str(pageHead.last().url)
		#Read of Alexa's page for scraping
		page = urlopen(lastPage).read()
		#Source code of the page
		soup = BeautifulSoup(page, 'html.parser')
		#Saves the rows  of the table that have site-listing class which
		#contains all information that we need to show
		table= soup.findAll(class_="site-listing")
		#Counter for calculate position
		i=0
		#Iterate for every row that we found in table
		for row in table: 
			i+=1
			#Look for DescriptionCell class inside every row. 
			#DescriptionCell class contains name, url and description.
			for link in row.findAll( class_="DescriptionCell"):
				#Creation of a dictionary
				info={}
				#We obtain the tag a who has url that we want to. 
				url= link.find('a', href= True)
				#Search information about the url
				description= link.find(class_="description")
				#Remove link "<a> less </a>" in the description
				for a in description("a"):
					description.a.extract()
				#Save information in the dictionary
				#Save the position of every page to maintain order
				info['position']= i
				info['name']= url.string
				#Get just de url
				info['url']= url.get('href')
				info['description']=description.get_text()
				#Saving in the array
				dictDomains.append(info)

		#Get the last five url searched 
		fiveRecords = recentViews.objects.all().order_by('-id')[:5]

		#Return dictionary
		return render(request, 'alexaDomain.html', {'domains': dictDomains, 'recents': fiveRecords})

	def post(self, request,*args, **kwargs):
		#Get data from the input URL and saving in the database
		form = URLForm(request.POST)
		if form.is_valid():
			url = form.cleaned_data['nameURL']
			#if exist then we delete it and create again to show it as first 
			#if not just create it
			try:
				linkdelete = recentViews.objects.get(url=url).delete()
				link = recentViews.objects.create(url=url)
			except recentViews.DoesNotExist:
				link = recentViews.objects.create(url=url)
			#Return main page
			return HttpResponseRedirect("/")
		else:
			#if something goes wrong show the message
			print(form.errors)
			messages.add_message(request, messages.ERROR, "Ha ocurrido un error")
			HttpResponseRedirect("/")

