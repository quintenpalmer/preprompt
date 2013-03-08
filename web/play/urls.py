from django.conf.urls import patterns, include, url

from . import views

urlpatterns = patterns('',
	url(r'^$',views.splash),
	url(r'^games/$',views.games),
	url(r'^game/(\d+)/$',views.game),
	url(r'^games/ajax_new_game/$',views.ajax_new_game),
	url(r'^manage/$',views.manage),
	url(r'^manage/cards/$',views.cards),
	url(r'^manage/decks/$',views.decks),
	url(r'^manage/decks/(\d)/$',views.deck),
	url(r'^manage/decks/new/$',views.deck_new),
)
