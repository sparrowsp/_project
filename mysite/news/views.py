from django.shortcuts import render
from django.shortcuts import HttpResponse

def show_news(request, news_id=0, cat_id=0):

    resp = HttpResponse('Category {}, Article {}'.format(cat_id, news_id))
    return resp