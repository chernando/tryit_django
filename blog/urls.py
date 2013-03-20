# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^publish/$', views.post_create, name='publish'),
    url(r'^post/(?P<post_id>\d+)/$', views.post_detail, name='post'),
    url(r'^post/(?P<post_id>\d+)/comment/$', views.comment_create, name='comment'),

    # XXX: For dear devops:
    url(r'^alive/$', views.alive, name='alive'),
)
