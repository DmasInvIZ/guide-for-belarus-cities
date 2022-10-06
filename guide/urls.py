from django.urls import path
from guide.views import news_view, AboutView, what_to_watch_view, town_view, district_view
from django.conf import settings

urlpatterns = [
    # path('', NewsView.as_view()),
    path('', news_view),
    # path('about/', about_view),
    path('about/', AboutView.as_view()),
    # path('what-to-watch/', WhatToWatchView.as_view()),
    path('districts/', what_to_watch_view),     # вывод всех областей страны из бд
    path('district/<int:pk>', district_view),   # вывод всех внесенных городов в данную область страны
    path('town/<int:pk>', town_view),          # вывод конкретного города по запросу
]
