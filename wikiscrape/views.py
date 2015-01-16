from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

import wikipedia
import requests
import bs4
import json

def index(request):
	return render(request, 'index.html')

def about(request):
	return render(request, 'about.html')

def search(request):
	print request.GET['search']
	result = wikipedia.page(title=wikipedia.search(request.GET['search']))
	wikiPages = result.links
	extPages = result.references
	response1 = ""
	response2 = ""

	for page in wikiPages:
		response1 += page
		response1 += "\n"
	for page in extPages:
		response2 += page
		response2 += "\n"

	return HttpResponse(response1 + "<br><br>" + response2)

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
