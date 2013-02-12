from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'games.views.index'),
    url(r'^game$', 'games.views.game'),
    url(r'^about$', 'games.views.about'),
    url(r'^account$', 'games.views.account'),
    url(r'^css/([A-Za-z]+.css)$', 'games.views.getcss'),
    # url(r'^postprompt/', include('postprompt.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
