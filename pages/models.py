from django.db import models

class WikipediaPage(models.Model):
	page_title = models.CharField(max_length=200)

	#Creates a many-to-one relationship with itself. (parent-child)
	parent_page = models.ForeignKey('self', default='')



class OtherPage(models.Model):
	links = models.ManyToManyField(WikipediaPage)
