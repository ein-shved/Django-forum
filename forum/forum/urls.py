from django.conf.urls import patterns, include, url
from django.contrib import admin
import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'forum.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'forum.views.index', name='index'),
    url(r'^login/$', 'forum.views.login', name='login'),
    url(r'^logout/$', 'forum.views.logout', name='logout'),
    url(r'^forum/$', views.Forum.as_view(), name='forum'),
    url(r'^forum/(?P<pk>\d+)/$', views.TopicView.as_view(), name='topic'),
    url(r'^forum/(?P<pk>\d+)/reply$', views.reply, name='reply'),
    url(r'^register/$', 'forum.views.register', name='register'),
    url(r'^forum/create$', views.create, name='create'),
    url(r'^admin/$', include(admin.site.urls)),
)
