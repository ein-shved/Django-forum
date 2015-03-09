from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'forum.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'forum.views.index', name='index'),
    url(r'^login/', 'forum.views.login', name='login'),
    url(r'^forum/', 'forum.views.forum', name='forum'),
    url(r'^admin/', include(admin.site.urls)),
)
