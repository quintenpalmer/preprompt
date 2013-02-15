from django.conf.urls import patterns, include, url

from . import views

urlpatterns = patterns('',
	url(r'^$',views.game_splash),
	url(r'^play/$',views.game_play),
	url(r'^manage/$',views.game_manage),
)
