from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.views.generic import ListView, DetailView
from django.shortcuts import render, redirect

from django.utils.decorators import method_decorator

from .models import *

from .forms import SuggestForm

from django.contrib import messages


# главная страница, на ней новости
class NewsView(ListView):
    model = News
    template_name = 'main.html'
    context_object_name = 'news'
    ordering = '-date'  # сортировка новостей по дате создания (новые сверху)


# детали новостей
class NewsDetailView(DetailView):
    model = News
    template_name = 'news_detail.html'


# страница "О проекте"
@method_decorator(login_required, name='dispatch')
class AboutView(ListView):
    model = About
    template_name = 'about.html'
    context_object_name = 'posts'
    ordering = '-date'


# страница со списком всех внесенных областей страны
def what_to_watch_view(request):
    districts = Districts.objects.all().order_by('name')
    return render(request, 'districts.html', context={'districts': districts})


# выводим список всех внесенных городов в запрошенной области
def towns_view(request, pk):
    towns = Towns.objects.filter(district_id=pk).order_by('name')
    return render(request, 'towns.html', context={'towns': towns})


# выводим город по запросу (что посмотреть)
@login_required
def town_watch_view(request, pk):
    town = Towns.objects.get(id=pk)
    pub_town_watch = UserTowns.objects.filter(town_id=pk, is_published=True)  # убран параметр town_id=pk
    context = {
        'town_watch': town,
        'pub_town_watch': pub_town_watch,
    }
    return render(request, 'town_watch.html', context)


# выводим город по запросу (где поесть)
@login_required
def town_eat_view(request, pk):
    town = Towns.objects.get(id=pk)
    pub_town_eat = UserTowns.objects.filter(town_id=pk, is_published=True)  # ищет запись в таблице предложений от юзеров (где поесть)
    context = {
        'town_eat': town,
        'pub_town_eat': pub_town_eat,
    }
    return render(request, 'town_eat.html', context)


# выводим город по запросу (где поспать)
@login_required
def town_sleep_view(request, pk):
    town = Towns.objects.get(id=pk)
    pub_town_sleep = UserTowns.objects.filter(town_id=pk, is_published=True)  # ищет запись в таблице предложений от юзеров (где поспать)
    context = {
        'town_sleep': town,
        'pub_town_sleep': pub_town_sleep,
    }
    return render(request, 'town_sleep.html', context)


# страница предложения публикации инфы о городах от пользователей
@login_required
def publish_suggest_view(request):
    if request.method == 'POST':
        form = SuggestForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.author = request.user
            form.save()
            messages.success(request, 'Отлично, ваша публикация отправлена на модерацию.')
            return redirect('/suggest')
        else:
            messages.warning(request, 'Что-то не так, проверьте, все ли поля заполнены?')
    else:
        form = SuggestForm()
    return render(request, 'suggest.html', {'form': form})


# поиск по городам
class SearchResultsView(ListView):
    model = Towns
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        towns_list = Towns.objects.filter(Q(name__icontains=query))
        return towns_list
