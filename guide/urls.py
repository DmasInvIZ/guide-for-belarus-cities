from django.urls import path
from guide.views import news_view, about_view, what_to_watch_view

urlpatterns = [
    # path('', NewsView.as_view()),
    path('', news_view),
    path('about/', about_view),
    # path('what-to-watch/', WhatToWatchView.as_view()),
    path('what-to-watch/', what_to_watch_view),
]
