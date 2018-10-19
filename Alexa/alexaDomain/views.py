from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import render
from bs4 import BeautifulSoup
from urllib.request import urlopen
from django.template import RequestContext
# Create your views here.




class Domain(TemplateView):
	# Main page
	template_view = "alexaDomain.html"

	def get(self, request, *args, **kwargs):
		# Array of distionaries. It will return the result to the view
		dictDomains=[]
		#Read of Alexa's page for scraping
		page = urlopen('https://www.alexa.com/topsites').read()
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
		#Return dictionary
		return render(request, 'alexaDomain.html', {'domains': dictDomains})
	