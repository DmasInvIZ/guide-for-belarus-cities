from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.shortcuts import render
# from .forms import SearchForm
# from haystack.query import SearchQuerySet

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
#     template_name = 'districts.html'
#     context_object_name = 'districts'


def what_to_watch_view(request):
    districts = Districts.objects.all()
    return render(request, 'districts.html', context={'districts': districts})


def towns_view(request):
    towns = Towns.objects.all()
    return render(request, 'towns.html', context={'towns': towns})


###-------поиск по сайту------###


# def post_search(request):
#     form = SearchForm()
#     if 'query' in request.GET:
#         form = SearchForm(request.GET)
#         if form.is_valid():
#             cd = form.cleaned_data
#             results = SearchQuerySet().models(Districts).filter(content=cd['query']).load_all()
#             # count total results
#             total_results = results.count()
#     return render(request,
#                   'search.html',
#                   {'form': form,
#                    'cd': cd,
#                    'results': results,
#                    'total_results': total_results})
#