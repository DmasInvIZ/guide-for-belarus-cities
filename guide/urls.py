from django.urls import path
from guide.views import *


urlpatterns = [
    path('', NewsView.as_view()),  # выводим все новости
    # path('news/<int:pk>/', NewsDetailView.as_view(), name='news_detail'),  # детали новости
    path('news/<slug:slug>/', NewsDetailView.as_view(), name='news_detail'),  # детали новости с красивым URl
    path('about/', AboutView.as_view()),  # страница "О проекте"
    path('districts/', what_to_watch_view, name='districts'),  # вывод всех областей страны из бд
    path('<slug:slug>/', towns_view, name='towns'),  # вывод всех внесенных городов в данную область страны
    # path('towns/<int:pk>', TownsView.as_view()),
    path('town_watch/<slug:slug>', town_watch_view, name='town_watch'),  # вывод города по запросу (что посмотреть)
    path('town_eat/<slug:slug>', town_eat_view, name='town_eat'),  # вывод города по запросу (где поесть)
    path('town_sleep/<slug:slug>', town_sleep_view, name='town_sleep'),  # вывод  города по запросу (где поспать)
    # path('town_watch/<int:pk>', TownWatchView.as_view(), name='town_watch'),  ####
    # path('town_eat/<int:pk>', TownEatView.as_view(), name='town_eat'),  #####
    # path('town_sleep/<int:pk>', TownSleepView.as_view(), name='town_sleep'),  ####
    path('users/profile/suggest/', publish_suggest_view),  # предложения пользователей
    path('search/', SearchResultsView.as_view(), name='search_results'),  # страница поиска
]
