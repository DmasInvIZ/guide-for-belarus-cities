from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.views.generic import ListView
from django.shortcuts import render
from .models import About
from django.utils.decorators import method_decorator

from guide.models import News, Districts, Towns


# class NewsView(ListView):
#     model = News
#     template_name = 'base.html'
#     context_object_name = 'news'


# главная страница, на ней новости
def news_view(request):
    news = News.objects.all().order_by('-date')
    return render(request, 'main.html', context={'news': news})


# страница "О проекте"
@method_decorator(login_required, name='dispatch')
class AboutView(ListView):
    model = About
    template_name = 'about.html'
    context_object_name = 'posts'
    ordering = '-date'


# страница "о проекте"
# def about_view(request):
#     return render(request, 'about.html')


# class WhatToWatchView(ListView):
#     model = Districts
#     print('class watsup?')
#     template_name = 'districts.html'
#     context_object_name = 'districts'


# страница со списком внесенных областей страны
def what_to_watch_view(request):
    districts = Districts.objects.all().order_by('name')
    return render(request, 'districts.html', context={'districts': districts})


# выводим город по запросу (что посмотреть)
@login_required
def town_watch_view(request, pk):
    town = Towns.objects.get(id=pk)
    return render(request, 'town_watch.html', {'town_watch': town})


# выводим город по запросу (где поесть)
@login_required
def town_eat_view(request, pk):
    town = Towns.objects.get(id=pk)
    return render(request, 'town_eat.html', {'town_eat': town})


# выводим город по запросу (где поспать)
@login_required
def town_sleep_view(request, pk):
    town = Towns.objects.get(id=pk)
    return render(request, 'town_sleep.html', {'town_sleep': town})


# выводим список внесенных городов в запрошенной области
def district_view(request, pk):
    towns = Towns.objects.filter(district_id=pk).order_by('name')
    return render(request, 'district.html', context={'towns': towns})


# поиск по городам
class SearchResultsView(ListView):
    model = Towns
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Towns.objects.filter(Q(name__icontains=query))
        return object_list
