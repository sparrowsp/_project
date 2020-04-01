# -*- coding: utf-8 -*-

from django.contrib import admin
from django.conf.urls import url

from news.views import show_news

urlpatterns = [
    url(r'^(?P<cat_id>\d+)/(?P<news_id>\d+)/$', show_news, name='show_news'),
    url(r'^(?P<news_id>\d+)/$', show_news, name='show_news'),
    url(r'^(?P<news_id>\d+)/like/$', show_news, name='show_news'),
]