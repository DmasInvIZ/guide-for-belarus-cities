from django.urls import path
from guide.views import news_view, about_view, what_to_watch_view, towns_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('', NewsView.as_view()),
    path('', news_view),
    path('about/', about_view),
    # path('what-to-watch/', WhatToWatchView.as_view()),
    path('districts/', what_to_watch_view),
    path('towns/', towns_view),
]
