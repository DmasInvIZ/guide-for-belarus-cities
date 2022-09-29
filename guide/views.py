from django.views.generic import ListView
from django.shortcuts import render

from guide.models import News, Districts, Towns


# class NewsView(ListView):
#     model = News
#     template_name = 'base.html'
#     context_object_name = 'news'


def news_view(request):
    news = News.objects.all().order_by('-date')
    return render(request, 'main.html', context={'news': news})


def about_view(request):
    return render(request, 'about.html')


# class WhatToWatchView(ListView):
#     model = Districts
#     print('class watsup?')
#     template_name = 'what-to-watch.html'
#     context_object_name = 'districts'


def what_to_watch_view(request):
    districts = Districts.objects.all()
    return render(request, 'what-to-watch.html', context={'districts': districts})


def towns_view(request):
    towns = Towns.objects.all()
    return render(request, 'towns.html', context={'towns': towns})