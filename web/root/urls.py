from django.conf.urls import patterns, include, url
from django.shortcuts import render_to_response

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', include('home.urls')),
	url(r'^play/', include('play.urls')),
	url(r'^trade/', include('trade.urls')),
	url(r'^account/', include('account.urls')),
	url(r'^about/', include('about.urls')),
	url(r'^news/', include('news.urls')),
    # url(r'^postprompt/', include('postprompt.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
