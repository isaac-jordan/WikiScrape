from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

import wikipedia
import requests
import bs4
import json
from urlparse import urlparse

def index(request):
	return render(request, 'index.html')

def about(request):
	return render(request, 'about.html')

def search(request):
	print request.GET['search']
	result = wikipedia.page(title=wikipedia.search(request.GET['search']))
	
        url = result.url.decode()
        print url
	response = requests.get(url)
        soup = bs4.BeautifulSoup(response.text)
        links = [a.attrs.get('href') for a in soup.select('a.external')]
        domains = {}
        for link in links:
            domain = '{uri.scheme}://{uri.netloc}/'.format(uri=urlparse(link))
            if domain in domains:
                domains[domain] += 1
            else:
                domains[domain] = 1
        print domains
	return HttpResponse("Check the terminal!")

@csrf_exempt
def ajaxSuggest(request):
	return HttpResponse(
		json.dumps(wikipedia.search(request.POST['search'],
		results=3)),
		content_type='application/json'
	)


def searchWiki(url):
	response = requests.get(url)
	soup = bs4.BeautifulSoup(response.text)
	links = soup.select

