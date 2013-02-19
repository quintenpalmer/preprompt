from django.conf.urls import patterns, include, url

from . import views

urlpatterns = patterns('',
	url(r'^$',views.profile),
	url(r'^login/$',views.login_user),
	url(r'^logout/$',views.logout_user),
	url(r'^register/$',views.register_user),
	url(r'^require_login/$',views.require_login),
)
