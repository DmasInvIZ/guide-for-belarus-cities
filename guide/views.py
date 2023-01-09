from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.views.generic import ListView, DetailView
from django.shortcuts import render, redirect

from django.utils.decorators import method_decorator

from .models import *

from .forms import *

from django.contrib import messages


class NewsView(ListView):
    """Страница с новостями, пока на главной странице сайта"""
    model = News
    template_name = 'main.html'
    context_object_name = 'news'
    ordering = '-date'  # сортировка новостей по дате создания (новые сверху)

    # Меню сайта
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['districts'] = Districts.objects.all().order_by('name')
    #     return context


class NewsDetailView(DetailView):
    """Страница с деталями новости"""
    model = News
    template_name = 'news_detail.html'


@method_decorator(login_required, name='dispatch')
class AboutView(ListView):
    """Страница 'О проекте'"""
    model = About
    template_name = 'about.html'
    context_object_name = 'posts'
    ordering = '-date'


def what_to_watch_view(request):
    """Отображение всех областей страны"""
    districts = Districts.objects.all().order_by('name')
    return render(request, 'districts.html', context={'districts': districts})


# выводим список всех внесенных городов в запрошенной области
# class TownsView(ListView):
#     model = Districts
#     template_name = 'towns.html'
#     context_object_name = 'towns'
#     pk_url_kwarg = 'pk'
#
#     def get_queryset(self):
#         return Towns.objects.filter(district_id=pk).order_by('name')


def towns_view(request, slug):
    """Отображение городов в выбранной области"""
    towns = Towns.objects.filter(district_id=slug).order_by('name')
    context = {
        'towns': towns,
    }
    return render(request, 'towns.html', context)


@login_required
def town_watch_view(request, slug):
    """Выводим город по запросу (что посмотреть)"""
    town = Towns.objects.get(town_slug=slug)
    pub_town_watch = UserTowns.objects.filter(town_id=slug, is_published=True)
    context = {
        'town_watch': town,
        'pub_town_watch': pub_town_watch,
    }
    return render(request, 'town_watch.html', context)


@login_required
def town_eat_view(request, slug):
    """Выводим город по запросу (где поесть)"""
    town = Towns.objects.get(town_slug=slug)
    pub_town_eat = UserTowns.objects.filter(town_id=slug, is_published=True)
    context = {
        'town_eat': town,
        'pub_town_eat': pub_town_eat,
    }
    return render(request, 'town_eat.html', context)


@login_required
def town_sleep_view(request, slug):
    """Выводим город по запросу (где поспать)"""
    town = Towns.objects.get(town_slug=slug)
    pub_town_sleep = UserTowns.objects.filter(town_id=slug, is_published=True)
    context = {
        'town_sleep': town,
        'pub_town_sleep': pub_town_sleep,
    }
    return render(request, 'town_sleep.html', context)


@login_required
def publish_suggest_view(request):
    """Форма ппредложения публикации инфы о городах от пользователей"""
    if request.method == 'POST':
        form = SuggestForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.author = request.user
            form.save()
            messages.success(request, 'Отлично, ваша публикация отправлена на модерацию.')
            return redirect('/users/profile/suggest')
        else:
            messages.warning(request, 'Что-то не так, проверьте, все ли поля заполнены?')
    else:
        form = SuggestForm()
    return render(request, 'suggest.html', {'form': form})


class SearchResultsView(ListView):
    """Поиск по городам"""
    model = Towns
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        towns_list = Towns.objects.filter(Q(name__icontains=query))
        return towns_list
