from django.urls import path
from guide.views import *  # NewsView, AboutView, what_to_watch_view, towns_view, SearchResultsView, \

# town_watch_view, town_eat_view, town_sleep_view, publish_suggest_view, NewsDetailView

urlpatterns = [
    path('', NewsView.as_view()),  # выводим все новости
    # path('news/<int:pk>/', NewsDetailView.as_view(), name='news_detail'),  # детали новости
    path('news/<slug:slug>/', NewsDetailView.as_view(), name='news_detail'),  # детали новости с красивым URl
    path('about/', AboutView.as_view()),  # страница "О проекте"
    path('districts/', what_to_watch_view, name='districts'),  # вывод всех областей страны из бд
    path('towns/<int:pk>', towns_view, name='towns'),  # вывод всех внесенных городов в данную область страны
    # path('towns/<int:pk>', TownsView.as_view()),
    path('towns/town_watch/<int:pk>', town_watch_view),  # вывод конкретного города по запросу (что посмотреть)
    path('towns/town_eat/<int:pk>', town_eat_view),  # вывод конкретного города по запросу (где поесть)
    path('towns/town_sleep/<int:pk>', town_sleep_view),  # вывод конкретного города по запросу (где поспать)
    # path('town_watch/<int:pk>', TownWatchView.as_view(), name='town_watch'),  ####
    # path('town_eat/<int:pk>', TownEatView.as_view(), name='town_eat'),  #####
    # path('town_sleep/<int:pk>', TownSleepView.as_view(), name='town_sleep'),  ####
    path('suggest/', publish_suggest_view),  # предложения пользователей
    path('search/', SearchResultsView.as_view(), name='search_results'),  # страница поиска
]
