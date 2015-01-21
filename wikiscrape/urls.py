from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'wikiscrape.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', index, name='index'),
    url(r'^search/', search),
    url(r'^ajaxSuggest/', ajaxSuggest),
    url(r'^about$', about, name='about'),
    #url(r'^admin/', include(admin.site.urls)),
)
