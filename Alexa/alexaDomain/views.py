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
		dictDomains=[]
		page = urlopen('https://www.alexa.com/topsites').read()
		soup = BeautifulSoup(page)
		table= soup.findAll(class_="site-listing")
		i=0
		for row in table: 
			i+=1
			for link in row.findAll('a', href=True):
				info={}
				info['position']= i
				info['name']= link.string
				info['url']= link.get('href')
				dictDomains.append(info)
		print(len(dictDomains))
		return render(
			request, 
			'alexaDomain.html', 
			{'domains': dictDomains},
			)
	