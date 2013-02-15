from django.conf.urls import patterns, include, url

from . import views

urlpatterns = patterns('',
	url(r'^$',views.profile),
	url(r'^login$',views.login),
	url(r'^logout$',views.logout),
	url(r'^register$',views.register),
)
