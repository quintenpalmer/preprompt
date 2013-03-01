from django.conf.urls import patterns, include, url

from . import views

urlpatterns = patterns('',
	url(r'^$',views.splash),
	url(r'^play/$',views.play),
	url(r'^play/(\d+)/$',views.game_view),
	url(r'^manage/$',views.manage),
	url(r'^manage/cards$',views.cards),
	url(r'^manage/decks$',views.decks),
)
