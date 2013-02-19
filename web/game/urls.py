from django.conf.urls import patterns, include, url

from . import views

urlpatterns = patterns('',
	url(r'^$',views.splash),
	url(r'^play/$',views.play),
	url(r'^manage/$',views.manage),
)
