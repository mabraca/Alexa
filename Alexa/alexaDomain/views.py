from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import render
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
from django.template import RequestContext
# Create your views here.




class Domain(TemplateView):
	template_view = "alexaDomain.html"

	def get(self, request, *args, **kwargs):
		dictDomains={}
		page = urlopen('https://www.alexa.com/topsites').read()
		soup = BeautifulSoup(page)
		table= soup.findAll(class_="site-listing")
		for row in table: 
			for link in row.findAll('a', href=True):
				dictDomains[link.string]=link.get('href')
		print(len(dictDomains.items()))
		return render(
			request, 
			'alexaDomain.html', 
			{'domains': dictDomains.items()},
			)
	