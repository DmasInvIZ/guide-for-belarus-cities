from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.shortcuts import render
from .models import About
# from .forms import SearchForm
# from haystack.query import SearchQuerySet


from guide.models import News, Districts, Towns


# class NewsView(ListView):
#     model = News
#     template_name = 'base.html'
#     context_object_name = 'news'


# главная страница, на ней новости
def news_view(request):
    news = News.objects.all().order_by('-date')
    return render(request, 'main.html', context={'news': news})


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
    districts = Districts.objects.all()
    return render(request, 'districts.html', context={'districts': districts})


# выводим город по запросу
def town_view(request, pk): ######################################################################
    town = Towns.objects.get(id=pk)
    return render(request, 'town.html', {'town': town})


# выводим список внесенных городов в запрошеной области
def district_view(request, pk):
    towns = Towns.objects.filter(district_id=pk)
    return render(request, 'district.html', context={'towns': towns})


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