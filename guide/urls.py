from django.urls import path
from guide.views import news_view, AboutView, what_to_watch_view, town_watch_view, district_view, SearchResultsView, \
    town_sleep_view, town_eat_view, publish_suggest_view

urlpatterns = [
    # path('', NewsView.as_view()),
    path('', news_view),
    # path('about/', about_view),
    path('about/', AboutView.as_view()),
    # path('what-to-watch/', WhatToWatchView.as_view()),
    path('districts/', what_to_watch_view),     # вывод всех областей страны из бд
    path('district/<int:pk>', district_view),   # вывод всех внесенных городов в данную область страны
    path('town_watch/<int:pk>', town_watch_view),          # вывод конкретного города по запросу (что посмотреть)
    path('town_eat/<int:pk>', town_eat_view),          # вывод конкретного города по запросу (где поесть)
    path('town_sleep/<int:pk>', town_sleep_view),          # вывод конкретного города по запросу (где поспать)
    path('suggest/', publish_suggest_view),
    path('search/', SearchResultsView.as_view(), name='search_results'),
]
